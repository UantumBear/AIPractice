# [REGION 1]
# python 스크립트를 실행하는 지점은 프로젝트의 루트 경로로 해야한다.
# PYTHONPATH=r"C:\Users\litl\PycharmProjects\gitProject\AIPractice"


# [REGION 2]
# 아래 파일 경로는 모든 프로젝트 사용자가 공용으로 사용하는 설정. 변경하지 않는다.
# 개별 API 접근용 키 설정은 env 파일로 관리하며 git에 공유하지 않는다.

import os
# Directory Path
ROOT_PATH=os.path.dirname(__file__)
CONFIG_PATH=os.path.join(ROOT_PATH, 'config')
print(f"ROOT_PATH: {ROOT_PATH}")
print(f"CONFIG_PATH: {CONFIG_PATH}")

# File Path
PROJECT_ENV_FILE_PATH=os.path.join(CONFIG_PATH, '../../config/project.env')
