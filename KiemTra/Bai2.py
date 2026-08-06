a = int(input("mặt hàng có giá là: "))
b = int(input("Số tiền khachs trả là: "))
tienThua = b-a
d = tienThua//20
e = (tienThua%20) //10
f = ( (tienThua%20) %10) //5
g = ( ((tienThua%20)%10)%5 )//2
h = ((((tienThua%20)%10)%5)%2)//1
dem = d+e+f+g+h
print(f"số tờ tiền phải trả la {dem}")
