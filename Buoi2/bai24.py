stations = list(map(float, input().split()))
k = int(input())

left = 0
right = stations[-1] - stations[0]

for _ in range(100):
    mid = (left + right) / 2

    need = 0

    for i in range(1, len(stations)):
        need += int((stations[i] - stations[i - 1]) / mid)

    if need > k:
        left = mid
    else:
        right = mid

print(round(right, 6))