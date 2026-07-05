def cau_5():
    print("\n--- Câu 5. Koko ăn chuối ---")

    def min_eating_speed(piles, h):
        def can_eat_all(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)  # Nếu dư vẫn tính tròn 1 giờ
            return hours <= h

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_eat_all(mid):
                ans = mid
                high = mid - 1  # Tìm tốc độ nhỏ hơn thỏa mãn
            else:
                low = mid + 1
        return ans

    piles = [3, 6, 7, 11]
    h = 8
    print(f"Các đống chuối: {piles}, Thời gian h = {h}")
    print(f"-> Tốc độ ăn tối thiểu: s = {min_eating_speed(piles, h)}")
