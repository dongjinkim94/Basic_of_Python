# 20190320
# 음수, 0, 양수 구별하기
# 사용자로부터 정수를 받아서 음수, 0, 양수 중의 하나로 분류하여 보자.

x = int(input("정수를 입력하시오: "))
if x == 0:
    print("입력된 정수는 0 입니다.")
elif x > 0:
    print("입력된 정수는 양수입니다.")
elif x < 0:
    print("입력된 정수는 음수입니다.")