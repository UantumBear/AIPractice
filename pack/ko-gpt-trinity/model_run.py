"""
GPU 가 있는 노트북에서 바로 실행되는 파일임
"""

from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import os
import torch
import csv

# Fx 2. GPU 사용 여부 확인
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU를 사용합니다.")
else:
    device = torch.device("cpu")
    print("GPU를 사용할 수 없습니다. CPU를 사용합니다.")

model_dir = "../../model/pretrained/skt/ko-gpt-trinity-1.2B-v0.5"
model = GPT2LMHeadModel.from_pretrained(model_dir)
tokenizer = GPT2TokenizerFast.from_pretrained(model_dir) # tokenizer 정의 없이 기본 값으로 다운로드.

# 모델을 GPU로 이동
model.to(device)
# tokenizer 는 이동시키지 않음. (토크나이저는 cpu에서 작동함.)

# Fx 1. 첫번째 테스트. 기본 문장 형태
# Step 1-1. 생성하려는 텍스트의 프롬프트
prompt = "개발곰은 귀엽다. 왜냐하면"

# Step 1-2. 토크나이저를 사용하여 프롬프트 인코딩
inputs = tokenizer.encode( prompt, return_tensors="pt",add_special_tokens=True)

# Step 1-3. gpu 로 inputs 데이터 이동
inputs = inputs.to(device)
# GPU에서 계산하려면(for model.generate) 계산에 넣을 값인 inputs 도 gpu로 이동시켜야 한다.
# tokenizer 는 CPU에 있으므로, tokenizer.encode 후 생성된 결과를 .to(device) 를 이용해서 GPU로 이동시킨다.

# Step 1-4-1 문장 생성
MAX_LENGTH = 40
NUM_RETURN_SEQUENCES = 2
NO_REPEAT_NGRAM_SIZE = 1
NUM_BEAMS = 3
EARLY_STOPPING = True
DO_SAMPLE = False
EOS_TOKEN_ID = 5 # 5:<unk>   tokenizer.eos_token_id

generated_text_samples_01 = model.generate(
    inputs,
    max_length=MAX_LENGTH,  # 생성할 텍스트의 최대 길이
    num_return_sequences=NUM_RETURN_SEQUENCES,  # 생성할 텍스트의 수
    no_repeat_ngram_size=NO_REPEAT_NGRAM_SIZE,  # 반복되는 n-gram 크기를 제한
    num_beams=NUM_BEAMS,
    early_stopping=EARLY_STOPPING,  # 조건을 만족하면 생성 중단
    do_sample=DO_SAMPLE,  # 빔 서치 사용
    eos_token_id=EOS_TOKEN_ID  # eos_token_id 사용하여 생성 중단

)
# Step 1-4-1-1. 생성된 텍스트 확인
# 생성된 텍스트를 디코딩하여 출력
generated_text = tokenizer.decode(
    generated_text_samples_01[0],
    skip_special_tokens=False
)
# 토큰 그대로 출력
print("생성된 문장: ", generated_text)
# 생성된 텍스트를 토크나이저로 다시 토큰화하여 출력
generated_tokens = tokenizer.encode(generated_text, add_special_tokens=False)
print("생성된 tokens: ", generated_tokens)
# 토큰을 단어로 변환하여 출력
tokens_to_words = tokenizer.convert_ids_to_tokens(generated_tokens)
print("단어로 치환: ", tokens_to_words)



# Fx 2. CSV 파일에 데이터를 추가하는 함수
def append_to_csv(file_path, data):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["prompt", "generated_text", "max_length", "num_return_sequences", "no_repeat_ngram_size", "num_beams", "early_stopping", "do_sample", "eos_token_id"])
        writer.writerow(data)

# CSV 파일에 데이터 추가
csv_file_path = "../../data/generated/text_config.csv"
append_to_csv(
    csv_file_path,
    data=[prompt, generated_text, MAX_LENGTH, NUM_RETURN_SEQUENCES, NO_REPEAT_NGRAM_SIZE, NUM_BEAMS, EARLY_STOPPING, DO_SAMPLE, EOS_TOKEN_ID])
