import os
save_directory = "../../model/pretrained/skt/ko-gpt-trinity-1.2B-v0.5"


if not os.path.exists(save_directory): # 디렉토리 생성 (없을 경우)
    os.makedirs(save_directory)