def bai_46(a):
    """Tính tổng số shift cho mảng lớn bằng cách đếm số cặp nghịch thế qua Merge Sort, O(n log n)[cite: 172, 173]."""
    def merge_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_and_count(arr, temp_arr, left, mid)
            inv_count += merge_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)
        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid: temp_arr[k] = arr[i]; i += 1; k += 1
        while j <= right: temp_arr[k] = arr[j]; j += 1; k += 1
        for x in range(left, right + 1): arr[x] = temp_arr[x]
        return inv_count

    temp = [0] * len(a)
    return merge_and_count(a, temp, 0, len(a) - 1)

