def tim_ten(ds, ten):

    ten = ten.lower()

    for i in range(len(ds)):

        if ds[i].lower() == ten:
            return i

    return -1


ds = ["An", "Binh", "Chau"]

ten = input("Nhap ten: ")

print(tim_ten(ds, ten))