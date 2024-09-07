# bear.py

from utilities.rabbit import Rabbit
# import sys
# import os
# # 현재 파일의 디렉토리 경로를 가져와서 'utilities' 경로를 추가
# current_dir = os.path.dirname(os.path.abspath(__file__))
# utilities_dir = os.path.join(current_dir)
# sys.path.append(utilities_dir)
#
# from utilities.rabbit import Rabbit

class Bear:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.rabbit_friend = None

    def make_friend(self, rabbit_name, rabbit_age, rabbit_color):
        self.rabbit_friend = Rabbit(rabbit_name, rabbit_age, rabbit_color)
        print(f"{self.name}이(가) 새로운 친구 {self.rabbit_friend.name}을(를) 만들었습니다.")

    def eat(self, food):
        print(f"{self.name}이(가) {food}을(를) 먹고 있습니다.")

    def sleep(self):
        print(f"{self.name}이(가) 자고 있습니다.")

    def roar(self):
        print(f"{self.name}이(가) 포효하고 있습니다.")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}, 색깔: {self.color}")
        if self.rabbit_friend:
            print("친구 토끼 정보:")
            self.rabbit_friend.info()

# 클래스 사용 예제
bear1 = Bear("곰돌이", 5, "갈색")
bear1.info()
bear1.eat("꿀")
bear1.roar()
bear1.sleep()

# 곰돌이가 토끼 친구를 만듭니다.
bear1.make_friend("바니", 2, "하얀색")
bear1.info()
