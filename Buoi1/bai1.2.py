def tim_kiem_phan_tu(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


array = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x1 = 110
kq1 = tim_kiem_phan_tu(array, x1)
print(f"Input : array = {array}\n        x = {x1};")
print(f"Output : {kq1}")
print(f"Phan tu tim thay duoc tai vi tri la: {kq1}\n----")
x2 = 185
kq2 = tim_kiem_phan_tu(array, x2)
print(f"Input : array = {array}\n        x = {x2};")
print(f"Output : {kq2}")
print("Phan tu ko duoc tim thay trong arr[]")