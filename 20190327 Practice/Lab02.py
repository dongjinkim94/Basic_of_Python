# 20190327 Lab 2
# 정수들의 합
# 1 부터 사용자가 입력한 수 n 까지 더해서 (1+2+3+4+5...n)을 계산하는 프로그램을 작성하여 보자.
# for 문을 사용하면 간명하게 합계를 구할 수 있다.
sum = 0

n = int(input("어디까지 계산할까요: "))

for i in range(1, n + 1):
    sum += i
print("1부터", n, "까지의 정수의 합=", sum)
