from diffusers import StableDiffusion3Pipeline as StableDiffusionPipeline
import torch
import time
import os
from dir import ROOT_PATH
from dotenv import load_dotenv
load_dotenv()
print(f"허깅페이스토큰: {os.getenv("HUGGINGFACE_TOKEN")}")
class StableDiffusion:
    def __init__(self):
        """
        Stable Diffusion 클래스 초기화.
        :param model_id: Hugging Face 모델 ID (기본값: "stabilityai/stable-diffusion-3").
        :param local_dir: 모델을 저장할 로컬 디렉토리 경로.
        :param use_cuda: CUDA(GPU)를 사용할지 여부 (기본값: True).
        """
        self.model_id = "stabilityai/stable-diffusion-3-medium-diffusers" # 원본 모델 참조 이름
        self.pretrained_dir = f"{ROOT_PATH}/store/pretrained/stabilityai" # 원본 모델을 저장한 로컬 경로
        self.modified_dir = f"{ROOT_PATH}/store/modified/stabilityai"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = None

    def download_model(self):
        """
        모델을 Hugging Face에서 로컬 디렉토리로 다운로드하고 초기화합니다.
        """
        print(f"모델 {self.model_id}을(를) 다운로드하여 {self.pretrained_dir}에 저장합니다...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16,
            cache_dir=self.pretrained_dir,
            use_auth_token=os.getenv("HUGGINGFACE_TOKEN"),
            device_map="auto"
        )
        self.pipe = self.pipe.to(self.device)
        print("모델 다운로드 및 초기화 완료.")

    def load_model(self):
        """
        로컬에 저장된 모델을 불러옵니다.
        """
        print(f"로컬 경로 {self.pretrained_dir}에서 모델을 불러옵니다...")
        self.pipe = StableDiffusionPipeline.from_pretrained(
            #self.pretrained_dir,  # 로컬 경로에서 불러옴
            f"{self.pretrained_dir}/models--stabilityai--stable-diffusion-3-medium-diffusers/snapshots/ea42f8cef0f178587cf766dc8129abd379c90671",
            torch_dtype=torch.float16
        )
        self.pipe = self.pipe.to(self.device)
        print("모델 로드 완료.")

    def generate_image(self, prompt, output_path="generated_image.png"):
        """
        텍스트 프롬프트를 기반으로 이미지를 생성하고 저장합니다.
        :param prompt: 이미지 생성에 사용할 텍스트 프롬프트.
        :param output_path: 생성된 이미지를 저장할 경로 (기본값: "generated_image.png").
        """
        if not self.pipe:
            raise Exception("모델이 로드되지 않았습니다. download_model() 메서드를 먼저 실행하세요.")

        print(f"'{prompt}' 프롬프트를 기반으로 이미지를 생성 중입니다...")
        ##  PROBLEM. 시간이 너무 오래 걸렸다.
        # image = self.pipe(
        #     prompt=prompt,
        #     num_inference_steps=30,
        #     height=512, width=512,
        # ).images[0]
        ## PROBLEM. # Mixed Precision 기법은 out of memory 가 발생한다.
        # with torch.cuda.amp.autocast():
        #     image = self.pipe(
        #         prompt=prompt,
        #         num_inference_steps=30,
        #         height=512, width=512,
        #     ).images[0]
        # 시간 기록 시작
        start_time = time.time()
        image = self.pipe(
                prompt=prompt,
                num_inference_steps=50,
                height=512, width=512
            ).images[0]
        # 시간 기록 종료
        end_time = time.time()

        # 시간 차이 계산
        elapsed_time = end_time - start_time
        print(f"이미지 생성 완료! 소요 시간: {elapsed_time:.2f}초")

        image.save(output_path)
        print(f"이미지가 {output_path}에 저장되었습니다.")
        image.show()
        # python model/stable_diffusion/model_run.py


