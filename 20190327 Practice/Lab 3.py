# 20190327 Lab 3
# 팩토리얼 계산
# for 문을 이용하여서 팩토리얼을 계산해보자.
# 팩토리얼은 n!은 1부터 n까지 정수를 모두 곱한 것을 의미한다.
# 즉, n! = 1 X 2 X 3 X ... (n-1) X n 이다.

sum = 1;
n = int(input("정수를 입력하시오: "))
for i in range(1, n + 1):
    sum *= i
print(n, "!은 %.1f 이다." %sum)
