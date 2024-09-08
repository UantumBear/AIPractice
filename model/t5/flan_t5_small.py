import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
import os
import time
from dotenv import load_dotenv

# .env 파일에서 환경변수를 불러옵니다.
load_dotenv()
print(f"허깅페이스토큰: {os.getenv('HUGGINGFACE_TOKEN')}")

class FlanT5Small:
    def __init__(self):
        """
        Flan-T5-small 모델 초기화 클래스.
        """
        self.model_id = "google/flan-t5-small"  # 모델 ID
        self.pretrained_dir = "./store/pretrained/google/flan-t5-small"  # 모델 저장 경로
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = None
        self.model = None

    def download_model(self):
        """
        모델을 Hugging Face에서 로컬 디렉토리로 다운로드하고 초기화합니다.
        """
        print(f"모델 {self.model_id}을(를) 다운로드하여 {self.pretrained_dir}에 저장합니다...")
        self.tokenizer = T5Tokenizer.from_pretrained(
            self.model_id,
            cache_dir=self.pretrained_dir,
            token=os.getenv("HUGGINGFACE_TOKEN")
        )
        self.model = T5ForConditionalGeneration.from_pretrained(
            self.model_id,
            cache_dir=self.pretrained_dir,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            token=os.getenv("HUGGINGFACE_TOKEN"),
            device_map="auto"
        )
        # self.model = self.model.to(self.device) #  device_map="auto" 옵션을 사용하면 자동으로 쓸 수 있는 기기에 저장
        print("모델 다운로드 및 초기화 완료.")

    def load_model(self):
        """
        로컬에 저장된 모델을 불러옵니다.
        """
        print(f"로컬 경로 {self.pretrained_dir}에서 모델을 불러옵니다...")
        self.tokenizer = T5Tokenizer.from_pretrained(
            f"{self.pretrained_dir}/models--google--flan-t5-small/snapshots/0fc9ddf78a1e988dac52e2dac162b0ede4fd74ab"
        )
        self.model = T5ForConditionalGeneration.from_pretrained(
            f"{self.pretrained_dir}/models--google--flan-t5-small/snapshots/0fc9ddf78a1e988dac52e2dac162b0ede4fd74ab",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )
        self.model = self.model.to(self.device)
        print("모델 로드 완료.")

    def generate_text(self, prompt, max_length=50):
        """
        텍스트 프롬프트를 기반으로 텍스트를 생성하고 반환합니다.
        :param prompt: 텍스트 생성에 사용할 프롬프트.
        :param max_length: 생성할 텍스트의 최대 길이 (기본값: 50).
        """
        if not self.model or not self.tokenizer:
            raise Exception("모델이 로드되지 않았습니다. download_model() 또는 load_model()을 먼저 실행하세요.")

        print(f"'{prompt}' 프롬프트를 기반으로 텍스트를 생성 중입니다...")

        # 시간 기록 시작
        start_time = time.time()

        # 입력 텍스트를 토큰화하고 텐서로 변환합니다.
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        # 모델을 통해 텍스트 생성
        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=max_length,
            num_return_sequences=1,
            early_stopping=True
        )

        # 생성된 텍스트 디코딩
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # 시간 기록 종료
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"텍스트 생성 완료! 소요 시간: {elapsed_time:.2f}초")
        print(f"생성된 텍스트: {generated_text}")

        return generated_text