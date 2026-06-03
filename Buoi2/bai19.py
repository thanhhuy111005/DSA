stalls = list(map(int, input().split()))
c = int(input())

stalls.sort()

left = 1
right = stalls[-1] - stalls[0]

ans = 0

while left <= right:
    mid = (left + right) // 2

    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= mid:
            count += 1
            last = stalls[i]

    if count >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)