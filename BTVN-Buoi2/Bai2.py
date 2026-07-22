a = int(input("Nhập ngày sinh : "))
b = int(input("Nhập tháng sinh : "))
c = int(input("Nhập năm sinh : "))
if a in [1,3,5,7,8,10,12]:
    if a<1 or a>31:
        print(f"Ngày không hợp lệ")
    else:
        if b==1:
            if a<=19:
                print(f"Ma Kết")
            else:
                print(f"Bảo Bình")
        elif b==3:
            if a<=20:        
                print(f"Song Ngư")
            else:
                print(f"Bạch Dương")  
        elif b==5:
            if a<=20:        
                print(f"Kim Ngưu")
            else:
                print(f"Song Tử")          
        elif b==7:
            if a<=22:        
                print(f"Cự Giải")
            else:
                print(f"Sư Tử")          
        elif b==8:
            if a<=22:        
                print(f"Sư Tủ")
            else:
                print(f"Xử Nữ")          
        elif b==10:
            if a<=22:        
                print(f"Thiên Bình")
            else:
                print(f"Bọ Cạp")          
        else:
            if a<=21:        
                print(f"Nhân Mã")
            else:
                print(f"Ma Kết")          
                  
elif a in [4,6,9,11]:
    if a<1 or a>30:
        print(f"Ngày không hợp lệ")
    else:
        if b==4:
            if a<=19:
                print(f"Bạch Dương")
            else:
                print(f"Kim Ngưu")
        elif b==6:
            if a<=20:        
                print(f"Song Tử")
            else:
                print(f"Cự Giải") 
        elif b==9:
            if a<=22:        
                print(f"Xử Nữ")
            else:
                print(f"Thiên Bình")        
        else:
            if a<=21:        
                print(f"Bọ Cạp")
            else:
                print(f"Nhân Mã")
else:
    if c/4==0 or c/100!= 0:
        if a<1 or a>29 :
            print(f"Ngày không hợp lệ")
        else:
            if a<=18:
                print(f"Bảo Bình")
            else:
                print(f"Song Ngư") 
    else :
        if a<0 or a>28:
            print(f"Ngày không hợp lệ")
        else:    
            if a<=18:
                print(f"Bảo Bình")
            else:
                print(f"Song Ngư")