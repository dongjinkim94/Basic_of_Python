# 20190327 Lab 13
# 배수의 합 계산 프로그램
# 1부터 100 사이의 모든 3의 배수의 합을 계산하여 출력하는 프로그램을 반복 구조를 사용하여 작성하라.

i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        sum += i
    i += 1

print("1부터 100 사이의 모든 3의 배수의 합은 %d 입니다." % sum)
