# 1
import functools
import operator

naturalNum = []
for x in range(1, 101):  # 1 upto 101, without 101
    naturalNum.append(x)

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, naturalNum))
