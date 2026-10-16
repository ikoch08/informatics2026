w = [int(x) for x in input().split()]
c = int(input())
n = len(w)
s = []
r = c
d = [[0] * (c + 1) for z in range(n + 1)]

for i in range(1, n + 1):
    x = w[i - 1]

    for j in range(c + 1):
        d[i][j] = d[i - 1][j]

        if x <= j:
            y = x + d[i - 1][j - x]
            d[i][j] = max(d[i][j], y)
for i in range(n, 0, -1):
    if d[i][r] != d[i - 1][r]:
        s.append(i)
        r -= w[i - 1]

s.reverse()
print(d[n][c], s)







