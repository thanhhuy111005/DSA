danh_ba = []

while True:

    print("\n1. Them lien he")
    print("2. Tim so dien thoai theo ten")
    print("3. Tim ten theo so dien thoai")
    print("4. Dem so lien he")
    print("5. Thoat")

    chon = input("Chon: ")

    if chon == "1":

        ten = input("Nhap ten: ")
        sdt = input("Nhap so dien thoai: ")

        danh_ba.append([ten, sdt])

    elif chon == "2":

        ten = input("Nhap ten can tim: ")

        found = False

        for item in danh_ba:

            if item[0] == ten:
                print("So dien thoai:", item[1])
                found = True
                break

        if found == False:
            print("Khong tim thay")

    elif chon == "3":

        sdt = input("Nhap so dien thoai: ")

        found = False

        for item in danh_ba:

            if item[1] == sdt:
                print("Ten:", item[0])
                found = True
                break

        if found == False:
            print("Khong tim thay")

    elif chon == "4":

        print("So lien he:", len(danh_ba))

    elif chon == "5":

        break

    else:

        print("Lua chon khong hop le")