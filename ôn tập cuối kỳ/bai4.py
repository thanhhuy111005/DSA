T = [73,74,75,71,69,72,76,73]

answer = [0] * len(T)
stack = []

for i in range(len(T)):
    while stack and T[i] > T[stack[-1]]:
        index = stack.pop()
        answer[index] = i - index

    stack.append(i)

print(answer)