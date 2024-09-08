from dotenv import load_dotenv
import os, sys
import torch

# 파이썬 패스는 구동 하는 파일에서 설정한다. (프로젝트 구조 정해지면 수정 할 것) START
PYTHONPATH = r"C:\Users\litl\PycharmProjects\gitProject\AIPractice"
os.environ['PYTHONPATH'] = PYTHONPATH
sys.path.append(PYTHONPATH) # sys.path에 추가하여 Python이 모듈을 찾을 수 있도록 설정
# END

from utils.com.logging_manager import LoggingManager
LOGGER = LoggingManager().get_logger()

from model.stable_diffusion.stable_diffusion import StableDiffusion


if __name__ == "__main__":
    if torch.cuda.is_available():
        print(f"사용 중인 GPU: {torch.cuda.get_device_name(torch.cuda.current_device())}")
    else:
        print("GPU가 사용 불가능하여 CPU를 사용 중입니다.")

    # StableDiffusion 클래스 인스턴스화
    sd_model = StableDiffusion()

    # 모델 다운로드
    # sd_model.download_model()

    # 모델 로드
    sd_model.load_model()


    # 이미지 생성
    sd_model.generate_image("Please create an image of a gray teddy bear-shaped robot wearing a white hat that looks like an antenna.")  # 이미지 생성

# python model/stable_diffusion/model_run.py
# pip show torch torchvision torchaudio
# pip uninstall torch torchvision torchaudio
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121