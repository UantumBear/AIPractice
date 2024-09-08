import os, sys
# 파이썬 패스는 구동 하는 파일에서 설정한다. (프로젝트 구조 정해지면 수정 할 것) START
PYTHONPATH = r"C:\Users\litl\PycharmProjects\gitProject\AIPractice"
os.environ['PYTHONPATH'] = PYTHONPATH
sys.path.append(PYTHONPATH) # sys.path에 추가하여 Python이 모듈을 찾을 수 있도록 설정
# END

from utils.com.logging_manager import LoggingManager
LOGGER = LoggingManager().get_logger()


from model.t5.flan_t5_small import FlanT5Small

if __name__ == "__main__":
    flan_t5_model = FlanT5Small()

    # 1. 모델 다운로드 및 초기화
    # flan_t5_model.download_model()

    # 2. 또는 로컬 모델 로드
    flan_t5_model.load_model()

    # 3. 텍스트 생성
    prompt = "translate English to Korean: How are you?."

    generated_text = flan_t5_model.generate_text(prompt, max_length=50)
    print(generated_text)



# python model/t5/flan_t5_small_run.py