# 10

def max_num(n=0):
    num_list = []
    for i in range(n, n+101):
        num_list.append(i)
    return max(num_list)


print(max_num(23))
