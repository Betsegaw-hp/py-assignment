# 4
import math

arr1 = []
arr2 = []

# Algorithm 1


def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        arr2.append(a)  # 0
        arr2.append(b)  # 1
        for i in range(2, n+1):  # 2 - 50
            c = a + b
            a = b
            b = c
            arr2.append(c)


fib(50)

# Algorithm 2


def fn(n):
    C1x1 = (1/math.sqrt(5))*(math.pow((1 + math.sqrt(5))/2, n))
    C2x2 = (1/math.sqrt(5))*(math.pow((1 - math.sqrt(5))/2, n))
    An = C1x1 - C2x2
    return round(An)


for x in range(51):  # 0 - 50
    arr1.append(fn(x))


# check if two algorithms yield the same output
if arr1 == arr2:
    print(True)
print(arr1)
print(arr2)
