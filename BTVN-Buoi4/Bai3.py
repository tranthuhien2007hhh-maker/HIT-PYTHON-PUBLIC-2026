san_pham =[]
n =int(input("Nhập số lượng sản phẩm: "))

for i in range(n):
    print(f"\nNhập thông tin sản phẩm thứ {i+1}")
    ma_sp =int(input("Mã sản phẩm: "))
    ten_sp =input("Tên sản phẩm: ")
    danh_muc =input("Danh mục: ")
    gia =float(input("Giá: "))
    ton_kho =int(input("Tồn kho: "))
    sp = {"ma_sp": ma_sp, "ten_sp": ten_sp, "danh_muc": danh_muc, "gia": gia, "ton_kho": ton_kho}
    san_pham.append(sp)
    
print("\nDanh sách sản phẩm:")
print(san_pham)

dien_tu =list(filter(lambda sp : sp["danh_muc"] ==  "Điện tử",san_pham))

print(dien_tu)
het_hang =list(filter(lambda sp : sp["ton_kho"] ==0, san_pham))

print(het_hang)
ten = list(map(lambda sp : sp["ten_sp"], san_pham))

print(ten)
cao_cap = filter(lambda sp : sp["gia"] >= 1000000, san_pham)
khuyen_mai =list(map(lambda sp : f"Tặng voucher 100k cho khách mua {sp['ten_sp']}", cao_cap))

print(khuyen_mai)