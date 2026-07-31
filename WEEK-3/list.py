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
list_a=[0,1,2,3,4,5,6]
list_b= list_a[::2]
print(my_list[:])
print(my_list[2:6])
print(my_list[:5])
print(my_list[5:])
print(my_list[::2])
print(my_list[::-1])
print(my_list[1::2])
my_list[2:5] = [1, 2, 5]
print(my_list)