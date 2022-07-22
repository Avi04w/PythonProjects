import math

N = int(input())
P = list()
W = list()
D = list()
for i in range(N):
    p, w, d = map(int, input().split(" "))
    P.append(p)
    W.append(w)
    D.append(d)


def distance_travel(p, w, d):
    if p < c:
        final_p = c - d
        if c - p < d:
            steps = 0
        else:
            steps = final_p - p
    else:
        final_p = d + c
        if p - c < d:
            steps = 0
        else:
            steps = p - final_p

    t = steps * w
    return t


def get_total():
    total = 0
    for i in range(N):
        total += distance_travel(P[i], W[i], D[i])
    return total


avg = math.floor(sum(P) / len(P))
c = avg
min_total = get_total()
while True:
    c = c - 1
    next_total = get_total()
    if next_total < min_total:
        min_total = next_total
    else:
        break
if c != avg:
    c = avg
    while True:
        c = c + 1
        next_total = get_total()
        if next_total < min_total:
            min_total = next_total
        else:
            break

print(min_total)