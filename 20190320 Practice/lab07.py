# 20190320
# 인터넷 쇼핑몰에서 물건을 구입할 때, 구입액이 10만원 이상이면 5%의 할인을 해준다고 하자.
# 사용자에게 구입 금액을 물어보고 최종적으로 할인 금액과 지불 금액을 출력하는 프로그램을 작서해보자.

string = input("구입 금액을 입력하시오: ")
if float(string) > 100000:
    print("지불 금액은", int(0.95 * float(string)), "원입니다.")
else:
    print("지불 금액은 " + string + " 원입니다.")