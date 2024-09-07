class Rabbit:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self, food):
        print(f"{self.name}이(가) {food}을(를) 먹고 있습니다.")

    def sleep(self):
        print(f"{self.name}이(가) 자고 있습니다.")

    def hop(self):
        print(f"{self.name}이(가) 뛰고 있습니다.")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}, 색깔: {self.color}")

# 클래스 사용 예제
rabbit1 = Rabbit("바니", 2, "하얀색")
rabbit1.info()
rabbit1.eat("당근")
rabbit1.hop()
rabbit1.sleep()
