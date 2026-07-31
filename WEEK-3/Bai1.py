n = int(input(f"nhap số sinh viên : "))
diem = []
for i in range(n):
    a = float(input(f"điẻm của hoc sinh {i+1} la : "))
    diem.append(a)
    print(diem)
tong =0

for a in diem:
    tong += a
    print("điểm trung bình : ", tong/n)
 
max = diem[0]
for a in diem:
    if a > max:
        max = a
        print(f"diểm lón nhất : {max}")

min = diem[0]
for a in diem:
    if a < min:
        min = a
        print(f"điểm bế nhất là {min}")

dem = 0
for a in diem:
    if a==10:
        print("có điẻm 10")
    else:
        print("Không có điểm 10")