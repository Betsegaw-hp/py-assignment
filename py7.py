# 7 is similar to #2
import random


def randomNumber():
    return int(random.random() * 100)


x = randomNumber()
y = randomNumber()
z = randomNumber()

print(x, ',', y, ',', z)
print("Largest Number : ", end="")
if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
elif z > x and z > y:
    print(z)

    # or
largest_number = max(x, y, z)
print("Largest Number : ", end="")
print(largest_number)
