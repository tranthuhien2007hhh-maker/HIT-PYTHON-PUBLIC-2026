import math
n = int(input("Nhâp số nguyên n : "))
tg = n
dem = 0
tong = 0
if tg ==0:
    dem = 1
else:
    if tg < 0:
        tg = -tg
    while tg > 0:
        dem +=1
        tg = tg//10
while tg > 0:
    tong += tg%10
    tg =tg//10    
if n<2:
    songuyento = False
else:
    songuyento = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            songuyento=False
            break   
print(f"Số chữ số :",dem)
print(f"Tổng các chữ số :",tong)
if songuyento:
    print(n,"là số nguyên tố")
else:
    print(n,"Không phải là số nguyên tố")
        