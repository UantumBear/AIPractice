from utilities.bear import Bear


# Bear 클래스의 인스턴스 생성
bear1 = Bear("곰돌이", 5, "갈색")

# Bear 인스턴스 사용 예제
bear1.info()
bear1.eat("꿀")
bear1.roar()
bear1.sleep()

# 곰돌이가 토끼 친구를 만듭니다.
bear1.make_friend("바니", 2, "하얀색")
bear1.info()