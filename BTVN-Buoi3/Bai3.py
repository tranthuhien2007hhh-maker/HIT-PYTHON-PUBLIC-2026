a = input("Nhập sở thích của A: ")
b = input("Nhập sở thích của B: ")

listA = []
for i in a.split(","):
    listA.append(i.strip().title())
    
listB = []
for i in b.split(","):
    listB.append(i.strip().title())
    
setA = set(listA)
setB = set(listB)

print(f"Các sở thích của Người A:")
print(setA)
print(f"\nCác sở thích của Người B:")
print(setB)
chung = setA & setB
print(f"\nSở thích chung:")

if len(chung) > 0:
    print(chung)
else:
    print(f"Không có sở thích chung.")
print(f"\nSở thích chỉ Người A có:")
print(setA - setB)

print(f"\nTất cả sở thích:")
tat_ca = setA | setB
print(tat_ca)

if len(tat_ca) == 0:
    do_tuong_dong = 0
else:
    do_tuong_dong = len(chung) / len(tat_ca) * 100
print(f"\nĐộ tương đồng: {do_tuong_dong:.2f}%")