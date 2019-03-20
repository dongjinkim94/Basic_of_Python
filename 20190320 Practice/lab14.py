# 20190320
# 윤년 판단
# 입력된 연도가 윤년인지 아닌지를 판단하는 프로그램을 만들어 보자.
# 윤년은 다음의 조건을 만족해야 한다.

# 연도가 4로 나누어 떨어지면 윤년이다.
# 100으로 나누어 떨어지는 연도는 제외한다.
# 400으로 나누어 떨어지는 연도는 윤년이다.

year = int(input("년도를 입력하시오: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("%d년은 윤년입니다." % year)
        else:
            print("%d년은 윤년이 아닙니다." % year)
    else:
        print("%d년은 윤년입니다." % year)
else:
    print("%d년은 윤년이 아닙니다." % year)