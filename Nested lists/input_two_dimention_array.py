n = int(input())

a = []

for i in range(n):
    a.append([int(j) for j in input().split()])

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
