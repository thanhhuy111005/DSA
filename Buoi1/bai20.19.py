ds = [
    {"ma": "SV01", "ten": "An", "dtb": 8.5},
    {"ma": "SV02", "ten": "Binh", "dtb": 7.8},
    {"ma": "SV03", "ten": "Chau", "dtb": 9.0}
]

ma_sv = input("Nhap ma SV: ")

found = False

for sv in ds:

    if sv["ma"] == ma_sv:

        print("Ma:", sv["ma"])
        print("Ten:", sv["ten"])
        print("DTB:", sv["dtb"])

        found = True
        break

if found == False:
    print("Khong tim thay")