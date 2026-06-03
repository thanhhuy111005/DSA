m, n = map(int, input().split())

matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))

x = int(input())

left, right = 0, m * n - 1
found = False

while left <= right:
    mid = (left + right) // 2

    row = mid // n
    col = mid % n

    if matrix[row][col] == x:
        found = True
        break
    elif matrix[row][col] < x:
        left = mid + 1
    else:
        right = mid - 1

print(found)