import math
a = int(input("toa do diem x1: "))
b = int(input("toa do diem y1 :"))
c = int(input("toa do diem x2 : "))
d = int(input("toa do diem y2 : "))
distance = math.sqrt(pow(a-c,2)+pow(b-d,2))

print(f"đo dai AB la : {distance:.3f}")