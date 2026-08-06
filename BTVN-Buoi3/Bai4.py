n = int(input())
ds = []
for i in range(n):
    ten,tien,danh_muc = input().split(",")
    ds.append((ten.strip(),int(tien),danh_muc.strip()))
print(f"Danh sách các khoản chi:")
for i in ds:
    print(i)
    
tong = 0
for i in ds:
    tong += i[1]
    
print(f"\nTổng chi tiêu:",tong,"VNĐ")

thong_ke = {}
for ten, tien, dm in ds:
    if dm not in thong_ke:
        thong_ke[dm] = [0, 0]
        thong_ke[dm][0] += 1
        thong_ke[dm][1] += tien
        
print(f"\nThống kê theo danh mục:")

for dm in thong_ke:
    print()
    print(dm + ":")
    print(f"- Số khoản chi:", thong_ke[dm][0])
    print(f"- Tổng tiền:", thong_ke[dm][1],"VNĐ")
    
if tong > 5000000:
    print(f"\nChi tiêu vượt quá 5.000.000 VNĐ.")
    
lon_nhat = ds[0]
for i in ds:
    if i[1] > lon_nhat[1]:
        lon_nhat = i
print(f"\nKhoản chi có số tiền lớn nhất:")
print(lon_nhat)