san_pham= []
n = int(input("Nhập số lượng sản phẩm"))
for i in range(n):
    while True:
        ma = input(f"Nhập mã san pham {i+1}:")
        trung = False
        for sp in san_pham:
            if ma == sp[0]:
                trung = True
                break  
        if trung == False:
            break
ten = input("Nhap tên: ")
while True:
    gia = input("Nhap gia: ")
    if gia < 0:
        break

so_luong = input("Nhap so luong: ")
while True:
    if so_luong > 0:
        break
    
max = sp[0]
for a in sp:
    if a > max:
        max=a
        print("gia lon nhat :", max)
    
san_pham.append((ma,ten,gia,so_luong))   

    

