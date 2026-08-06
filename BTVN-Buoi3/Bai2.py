chuoi = input("Nhập các sản phẩm: ")
san_pham_can_tim = input("Nhập sản phẩm cần kiểm tra: ")

danh_sach = []
for sp in chuoi.split(","):
    sp = sp.strip().title()
    danh_sach.append(sp)
    

print(f"Danh sách sản phẩm:")
print(danh_sach)
print(f"\nTổng số sản phẩm đã mua:", len(danh_sach))

if len(danh_sach) % 2 == 1:
    print(f"\nSản phẩm ở vị trí giữa:", danh_sach[len(danh_sach) // 2])
    
tap = set(danh_sach)
max_dem = 0
for sp in tap:
    dem = danh_sach.count(sp)
    if dem > max_dem:
        max_dem = dem
nhieu_nhat = []

for sp in tap:
    if danh_sach.count(sp) == max_dem:
        nhieu_nhat.append(sp)
nhieu_nhat.sort()

print(f"\nCác sản phẩm được mua nhiều nhất:")
for sp in nhieu_nhat:
    print(f"{sp}: {max_dem} lần")
    
san_pham_can_tim = san_pham_can_tim.strip().title()
dem = danh_sach.count(san_pham_can_tim)
if dem > 0:
    print(f"\n{san_pham_can_tim} đã được mua {dem} lần.")
else:
    print(f"\n{san_pham_can_tim} chưa được mua.")
danh_sach.insert(0, "Bánh Nabati")

if "Sữa" in danh_sach:
    danh_sach.remove("Sữa")
print(f"\nDanh sách sau khi cập nhật:")
print(danh_sach)