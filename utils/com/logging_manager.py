import logging
import os

class LoggingManager:
    _instance = None  # 싱글톤 패턴을 위한 클래스 변수

    def __new__(cls, *args, **kwargs):
        """ 싱글톤 인스턴스 생성 (한 번만 생성되도록 보장) """
        if cls._instance is None:
            cls._instance = super(LoggingManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        """ 로거 초기화 설정 """
        self.logger = logging.getLogger("global_logger")
        self.logger.setLevel(logging.DEBUG)  # 기본 로그 레벨 설정 (DEBUG)

        # 콘솔 핸들러 설정
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_format)

        # 파일 핸들러 설정 (로그 파일에 기록)
        log_file = os.path.join(os.path.dirname(__file__), 'app.log')
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s '
            '[%(filename)s:%(funcName)s:%(lineno)d]'
        )
        file_handler.setFormatter(file_format)

        # 로거에 핸들러 추가
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """ 로거 인스턴스를 반환 """
        return self.logger

