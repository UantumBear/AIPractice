from transformers import GPT2LMHeadModel, GPT2TokenizerFast
# from transformers import AutoModel, AutoTokenizer
import os

# Fx 1. 모델 로드 전, 모든 모델 파일이 존재하는 지 체크하여 없으면 local에 저장.
# Step 1-1. huggingface 에 다운받을 model 이름과 local에 save할 directory 설정
model_name = "skt/ko-gpt-trinity-1.2B-v0.5"
save_directory = "../../model/pretrained/skt/ko-gpt-trinity-1.2B-v0.5"

if not os.path.exists(save_directory): # 디렉토리 생성 (없을 경우)
    os.makedirs(save_directory)

# Step 1-2. 모델과 토크나이저 파일이 이미 있는지 체크
model_files = ['config.json', 'generation_config.json', 'model.safetensors']
tokenizer_files = ['tokenizer.json', 'tokenizer_config.json', 'special_tokens_map.json']
model_exists = all(os.path.isfile(os.path.join(save_directory, f)) for f in model_files)
tokenizer_exists = all(os.path.isfile(os.path.join(save_directory, f)) for f in tokenizer_files)

model = None
tokenizer = None
device = None

# Step 1-3. 모델이나 토크나이저 파일 중 하나라도 없으면 다운로드 및 저장
if not model_exists or not tokenizer_exists:
    print("모델 또는 토크나이저 파일이 누락되었습니다. 다운로드를 시작합니다...")
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2TokenizerFast.from_pretrained(model_name) # tokenizer 정의 없이 기본 값으로 다운로드.

    print(f"Loaded model class: {model.__class__.__name__}")
    print(f"Loaded tokenizer class: {tokenizer.__class__.__name__}")
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)
    print(f"모델과 토크나이저가 성공적으로 다운로드 되었습니다. 저장경로: {save_directory}")
else:
    print("모든 파일이 이미 존재합니다. 추가 다운로드가 필요하지 않습니다.")