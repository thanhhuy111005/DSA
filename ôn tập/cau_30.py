def cau_30():
    print("\n--- Câu 30. Lập lịch round-robin ---")

    def round_robin_simulation(processes, quantum):
        # processes dạng: list các [tên_tiến_trình, thời_gian_chạy]
        queue = deque(processes)
        time_elapsed = 0
        completion_report = {}

        while queue:
            name, burst_time = queue.popleft()
            run_time = min(burst_time, quantum)
            time_elapsed += run_time
            burst_time -= run_time

            if burst_time > 0:
                queue.append((name, burst_time))  # Nếu chưa xong quay về cuối hàng đợi
            else:
                completion_report[name] = time_elapsed
        return completion_report

    procs = [("P1", 5), ("P2", 2), ("P3", 4)]
    q = 2
    print(f"Tiến trình: {procs}, Quantum = {q}")
    print(f"Thời điểm hoàn thành thực tế: {round_robin_simulation(procs, q)}")


# ==============================================================================
# 6. ARRAY LIST & THAO TÁC TRÊN MẢNG ĐỘNG
# ==============================================================================
