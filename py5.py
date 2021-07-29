# 5
# write down the decimal number and to continually divide-by-2 (two) to give a result and a remainder of either a “1” or a “0” until the final result equals zero

binary = []


def converter(n):
    if n == 0:
        binary.append(n)
    while(n != 0):
        result = int(n/2)
        reminder = int(n % 2)
        n = result
        binary.append(reminder)


converter(345)
binary.reverse()
print(binary)
