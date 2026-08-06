a = input("Nhập chuỗi: ")

daochuoi =""
for i in range(len(a)-1,-1,-1):
    daochuoi += a[i]
print(f"Chuỗi đảo ngược:", daochuoi)

sapxep = "".join(sorted(a))
print(f"Chuỗi sau khi sắp xếp:", sapxep)
if a == daochuoi:
    print(f"Đây là chuỗi đối xứng.")
else:
    print(f"Đây không phải là chuỗi đối xứng.")
    
tap_ky_tu = set(a)
max_dem = 0
for ch in tap_ky_tu:
    dem = a.count(ch)
    if dem > max_dem:
        max_dem = dem
        
ds = []
for ch in tap_ky_tu:
    if a.count(ch) == max_dem:
        ds.append(ch)
ds.sort()

print(f"Ký tự xuất hiện nhiều nhất:")
for ch in ds:
    print(ch, end=" ")
print()

print(f"Số lần xuất hiện:", max_dem)
nguyen_am = {'a','e','i','o','u'}

tap = set(a.lower())
if nguyen_am.issubset(tap):
    print(f"Chuỗi chứa có đủ 5 nguyên âm tiếng Anh.")
else:
    print(f"Chuỗi không chứa có đủ 5 nguyên âm tiếng Anh.")