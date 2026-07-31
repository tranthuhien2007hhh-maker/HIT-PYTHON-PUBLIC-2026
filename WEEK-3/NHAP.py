
list1 = []     #danh sách trống
list2 = [1,  2,  3.6, "HIT"]
#vị trí [0,  1,   2  ,3   ]
#   hoắc[-4,-3,  -2  ,-1]

print(list1)
print(list2)

print(type(list1)) #(type):kiểm tra kiểu dữ liệu >> kết quả trả về là "list"
print(type(list2))

print(list2[3]) #==print(list2[-1])

print(type(list2[2]))  #==> Class 'float'
print(type(list2[0]))  #          'int'
print(type(list2[3]))  #          'str'

print(len(list1)) #(len()):đếm có bao nhiêu phần tử
print(len(list2))  #==> 4 (có 4 phần tử)

#--------List Comprehension-----------#
a = [i for i in range(10)]  # Phân  tích: range(10) => lấy số từ 0-10
                            #             for i in range(10) => giá trị i sẽ chạy từ 0-10
                            #             [i for i in range(10)] => lấy i đưa vào List ==> [0,1,2,3,4,5,6,7,8,9]
print(a)
b = [x for x in a]
print(b)
c = [x ** 2 for x in a] #khi x=[0,1,2,3,4] ==> i=[0,1,4,9,16]
print(c)
d = [x for x in a if x % 2 ==0]# == [x for x in range(10) if x%2==0] => lấy các số chia hết ch0 2 ==> [0,2,4,6,8]
print(d)

## append("gia_tri") luôn chỉ THÊM 1 phần tử "gia_tri" vào sau List
list1.append("Python")
list2.append("Python")
print(f"list sau khi thêm phần tử 'Python' vào cuối list append(): {list1}") #==> ["Python"]
print(f"list sau khi thêm phần tử 'Python' vào cuối list append(): {list2}")
list2.append("java") #==> [1,2,3.6,"hit","Python","java"]

## insert(vị_trí,gia_tri) : có thể CHÈN vào bất kỳ vị trí nào
list2.insert(3,3) # insert(a, b) thêm phần tử `b` vào vị trí có chỉ số `a`
list2.insert(1,6)
print(list2)

list2.extend([5,6,7])
print(list2)

list3 = [i for i in range(5)]
print(list3)
example1 = list3.copy()
example1.append(5)
example2 = list3.copy()
example2.insert(-1,5)
example3 = list3.copy()
example3.insert(len(example3),5)
print(example1)
print(example2)
print(example3)

list3[0] = 3
print(list3)
list3[-1] = "Rắn"
print(list3)


list4 = [4,8,5,0,"Táo"]
print(f"pop(-1) trả về: {list4.pop(-1)}")
print(f"list sau khi xóa phần tử tại index '-1' pop(): {list4}")
print(f"remove() trả về: {list4.remove(4)}")
print(f"list sau khi xóa phần tử '4' đầu tiên remove(): {list4}")
print(f"clear() trả về: {list4.clear()}")
print(f"list sau khi dùng phương thức clear(): {list4}")


list_a = [1, 2, 'a', 2.3, 4, 5, 'b']
# print(len(list_a))

# Cách 1:
for i in range(len(list_a)):
    print(list_a[i], end = ' ')

print("\n")
# Cách 2:
for x in list_a:
    print(x, end = ', ')
    # Sao chép danh sách
a = [6, 3, 4]
b = a * 2
print(f"Nhân đôi list a: {b}")

c = [0]
d = c * 100
print(f"Số lượng phần tử của list d: {len(d)}")

# Đếm số lần xuất hiện của một giá trị trong danh sách
count_3 = b.count(3)
print(f"Số lượng phần từ '3' trong list: {count_3}")

# Tìm chỉ số của một giá trị
pos = b.index(4)
print(f"Vị trí đầu tiên của phần tử '4' trong list: {pos}")

# Đảo ngược danh sách
a.reverse()
print(f"list sau khi được đảo ngược: {a}")

# Sắp xếp danh sách
b.sort()
print(f"list sau khi được sắp xếp: {b}")



my_list = [x for x in range(10,101,10)]

print(my_list[:])

print(my_list[2:6])

print(my_list[:5])

print(my_list[5:])

print(my_list[::2])

print(my_list[::-1])

print(my_list[1::2])

my_list[2:5] = [1, 2, 5]
print(my_list)