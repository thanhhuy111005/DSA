n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input())

arr = []

for row in matrix:
    arr.extend(row)

arr.sort()

print(arr[k - 1])