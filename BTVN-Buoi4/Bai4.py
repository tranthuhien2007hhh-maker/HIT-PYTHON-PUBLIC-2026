hoc_sinh = []
n = int(input("Nhập số lượng học sinh: "))
for i in range(n):
    print(f"\nNhập thông tin học sinh thứ {i+1}")
    ten = input("Tên học sinh: ")
    toan = float(input("Điểm Toán: "))
    van = float(input("Điểm Văn: "))
    anh = float(input("Điểm Anh: "))
    hs = {"ten": ten, "diem": {"Toán": toan,"Văn": van,"Anh": anh}}
    hoc_sinh.append(hs)
print("\n1. Danh sách học sinh theo điểm Toán giảm dần:")

sap_xep_toan = sorted(hoc_sinh, key=lambda hs: hs["diem"]["Toán"],
    reverse=True
)

for hs in sap_xep_toan:
    print(hs["ten"], "-", hs["diem"]["Toán"])

print("\n2. Học sinh có điểm Anh cao nhất:")
gioi_anh = max(hoc_sinh,key=lambda hs: hs["diem"]["Anh"])

print(gioi_anh["ten"], "-", gioi_anh["diem"]["Anh"])

print("\n3. Danh sách theo tổng điểm giảm dần:")
tong_diem = sorted(hoc_sinh,key=lambda hs: (
    (hs["diem"]["Toán"] +
    hs["diem"]["Văn"] +
    hs["diem"]["Anh"]),
    hs["ten"]
    )
)

for hs in tong_diem:
    tong = hs["diem"]["Toán"] + hs["diem"]["Văn"] + hs["diem"]["Anh"]
    print(hs["ten"], "-", tong)

print("\n4. Danh sách học sinh giỏi:")
gioi = filter(lambda hs:
    hs["diem"]["Toán"] +
    hs["diem"]["Văn"] +
    hs["diem"]["Anh"] >= 24,
    hoc_sinh
)
gioi = sorted(gioi,key=lambda hs:
    hs["diem"]["Toán"] +
    hs["diem"]["Văn"] +
    hs["diem"]["Anh"],
    reverse=True
)
ten = list(map(lambda hs: hs["ten"],gioi))
print(ten)