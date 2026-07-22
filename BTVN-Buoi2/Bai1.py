a = int(input("Nhập tháng : "))
b = int(input("Nhập năm : "))
if a<1 or a>12:
    print("Không hợp lệ ")
else:
    if a in [1,3,5,7,8,10,12] :
        print(f"tháng {a} có 31 ngày ")
    elif a in [4,6,9,11]:
        print(f"tháng {a} có 30 ngày ")
    else:
        if b/4==0 or b/100!= 0:
            print(f"tháng {a} có 29 ngày ")
        else:
            print(f"tháng {a} có 28 ngày ")
