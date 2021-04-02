#재귀함수X, 리스트X
def fibonacci(n):
    if n <=1:
        return n
    else:
        f0 = 0
        f1 = 1
        for i in range(2,n+1):
            f2 = f0 + f1
            f0, f1 = f1, f2
        return f2
for i in range(101):
    print(fibonacci(i),end=' ')

#재귀함수O
# n이 커질수록 재귀함수 호출이 많아져 시간복잡도가 크게 증가한다.
def fibonacci_recursive(n):
    if n <= 1 :
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
print('\n')
for i in range(11):
    print(fibonacci_recursive(i),end=' ')

