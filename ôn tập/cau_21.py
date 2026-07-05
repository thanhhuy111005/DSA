def cau_21():
    print("\n--- Câu 21. Dấu ngoặc cân bằng ---")

    def is_balanced(s):
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or stack.pop() != mapping[char]:
                    return False
        return len(stack) == 0

    s1 = "([]{})"
    s2 = "([)]"
    print(f"Chuỗi '{s1}' -> Kết quả kiểm tra: {is_balanced(s1)}")
    print(f"Chuỗi '{s2}' -> Kết quả kiểm tra: {is_balanced(s2)}")
