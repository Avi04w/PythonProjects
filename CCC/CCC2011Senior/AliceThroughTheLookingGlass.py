t = int(input())


def max_y(a, b):
    if a >= 1:
        p = 5 ** (a - 1)
        location = b // p
        if location == 0 or location == 4:
            return 0
        elif location == 1 or location == 3:
            return 1 * p + max_y(a - 1, b % p)
        elif location == 2:
            return 2 * p + max_y(a - 1, b % p)
    return 0


y_list = []

for i in range(t):
    m, x, y = input().split(" ")
    m = int(m)
    x = int(x)
    y = int(y)

    if y < max_y(m, x):
        y_list.append("crystal")
    else:
        y_list.append("empty")

for i in y_list:
    print(i)