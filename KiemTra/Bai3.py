a = input()
a.split(" ")
d = input("nhập từ cần tìm: ")
e = []
for i in range(len(a)):
    if a[i]== d:
        e.append(i)
if len(e)==0:
    print(-1)
else:
    print(e)