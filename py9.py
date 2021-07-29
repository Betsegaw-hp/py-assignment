# 9

number_series = [1, 2, 3, 4, 5]


def sum(num):
    y = 0
    for x in num:
        x += y
        y = x
    return y


def avg(num):
    sum_of_num = sum(num)
    length_of_num = len(num)
    result = sum_of_num / length_of_num
    return result


print(sum(number_series))  # sum of the numbers
print(avg(number_series))  # average of the numbers
