# 20190313 프로그래밍 입문
# 대화하는 프로그램 만들기
# 사용자에게 이름을 물어보고 화면에 "OOO님 반갑습니다"와 같이 출력한다.
# 이어서 사용자의 나이를 물어보고 "10년 후면 30살이 되시는군요!"와 같이 출력하도록 파이썬 프로그램을 작성하라.

name = input("이름을 입력해 주세요: ")
print(name + "님 반갑습니다.")
age = int(input(name + "님 나이를 입력해주세요: ")) + 10
print("10년 후면", age, "살이 되시는군요!")