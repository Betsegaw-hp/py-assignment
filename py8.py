# 8

def award(m):
    rank = ("Distiniction", "Merit", "Pass", "Fail")

    if m >= 80:
        print(rank[0])
    elif m >= 60:
        print(rank[1])
    elif m >= 40:
        print(rank[2])
    elif m < 40:
        print(rank[3])


award(75)
