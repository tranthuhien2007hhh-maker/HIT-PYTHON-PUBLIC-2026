# a,b = input().split()
# print("nhập 2 số nguyên : ")
# print("a= ",a)
# print("b= ",b)
a = int(input("nhập số nguyên a: "))
b = int(input("nhập số nguyên b: "))

tong =a+b
hieu = a-b
thuong = a/b
tich = a*b
print(f"tổng: " ,tong)
print(f"thương: %.3f" % thuong)
print(f"hiệu: ",hieu)
print(f"tích: ",tich)