# 3
import random


def isPrime(n):
    if n <= 1:
        return False

    for x in range(2, n):
        if (n % x == 0):
            return False

    return True

def randomNumber():
    return int(random.random() * 100)

x = randomNumber()
if isPrime(x):
    print(x, "- is prime")
else:
    print(x, "- is not prime")
