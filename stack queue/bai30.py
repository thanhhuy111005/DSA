# Bài 30. Lập lịch xoay vòng (Round-Robin) [cite: 102, 103]
def bai30(processes, burst_time, quantum):
    n = len(processes)
    rem_bt = list(burst_time)
    t = 0
    queue = deque(range(n))
    completion_time = [0] * n
    
    while queue:
        i = queue.popleft()
        if rem_bt[i] > quantum:
            t += quantum
            rem_bt[i] -= quantum
            queue.append(i)
        else:
            t += rem_bt[i]
            completion_time[i] = t
            rem_bt[i] = 0
    return {processes[i]: completion_time[i] for i in range(n)}