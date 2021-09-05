n=int(input())
tri = []

for i in range(n+1):
    tri.append([1]+[0]*n)

for i in tri:
    print(i)

for i in range(1, n+1):
    for j in range(1, i+1):
        tri[i][j] = tri[i-1][j] + tri[i-1][j-1]

print('*'*10)

for i in range(0, n+1):
    for j in range(0, i+1):
        print(tri[i][j], end=' ')
    print()

