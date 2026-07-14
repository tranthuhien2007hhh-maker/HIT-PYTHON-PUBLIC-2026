1. Python là ngôn ngữ thông dịch.
Python được thực thi thông qua trình thông dịch (Python Interpreter).
Trình thông dịch sẽ đọc, dịch và thực thi mã nguồn từng phần mà không 
cần người lập trình biên dịch toàn bộ chương trình thành tệp thực thi (.exe) trước khi chạy.
Quá trình thực hiện có thể mô tả như sau:
    Mã nguồn Python (.py)
          ↓
   Python Interpreter
          ↓
     Thực thi chương trình
     
     
2.1. Các liểu dữ liệu trong Python
    | Kiểu dữ liệu | Tên trong Python | Ví dụ           |
    | ------------ | ---------------- | --------------- |
    | Số nguyên    | `int`            | `10`, `-5`      |
    | Số thực      | `float`          | `3.14`, `5.6`   |
    | Chuỗi        | `str`            | `"Hello"`       |
    | Logic        | `bool`           | `True`, `False` |
    | Danh sách    | `list`           | `[1,2,3]`       |
    | Bộ dữ liệu   | `tuple`          | `(1,2,3)`       |
    | Tập hợp      | `set`            | `{1,2,3}`       |
    | Từ điển      | `dict`           | `{"name":"An"}` |

VD:
    age = 19                  # int
    height = 1.65             # float
    name = "Hien"             # str
    isStudent = True          # bool
    scores = [8,9,10]         # list
    point = (10,20)           # tuple
    colors = {"red","blue"}   # set
    student = {
        "name":"Hien",
        "age":19
    }                          # dict
    
2.2. Các loại toán tử 
    a. Toán tử số học
    | Toán tử | Ý nghĩa              | Ví dụ    | Kết quả |
    | ------- | -------------------- | -------- | ------- |
    | `+`     | Cộng                 | `5 + 3`  | `8`     |
    | `-`     | Trừ                  | `5 - 3`  | `2`     |
    | `*`     | Nhân                 | `5 * 3`  | `15`    |
    | `/`     | Chia                 | `5 / 2`  | `2.5`   |
    | `//`    | Chia lấy phần nguyên | `5 // 2` | `2`     |
    | `%`     | Chia lấy dư          | `5 % 2`  | `1`     |
    | `**`    | Lũy thừa             | `2 ** 3` | `8`     |
    
    b. Toán tử so sánh    //kết quả chỉ có true/false
    | Toán tử | Ý nghĩa           | Ví dụ    |
    | ------- | ----------------- | -------- |
    | `==`    | Bằng              | `5 == 5` |
    | `!=`    | Khác              | `5 != 3` |
    | `>`     | Lớn hơn           | `5 > 3`  |
    | `<`     | Nhỏ hơn           | `5 < 3`  |
    | `>=`    | Lớn hơn hoặc bằng | `5 >= 5` |
    | `<=`    | Nhỏ hơn hoặc bằng | `5 <= 3` |

   c. Toán tử gán
    | Toán tử | Ý nghĩa             | Ví dụ     |
    | ------- | ------------------- | --------- |
    | `=`     | Gán                 | `a = 5`   |
    | `+=`    | Cộng rồi gán        | `a += 2`  |
    | `-=`    | Trừ rồi gán         | `a -= 2`  |
    | `*=`    | Nhân rồi gán        | `a *= 2`  |
    | `/=`    | Chia rồi gán        | `a /= 2`  |
    | `//=`   | Chia nguyên rồi gán | `a //= 2` |
    | `%=`    | Chia dư rồi gán     | `a %= 2`  |
    | `**=`   | Lũy thừa rồi gán    | `a **= 2` |

   d. Toán tử logic
    | Toán tử | Ý nghĩa  |
    | ------- | -------- |
    | `and`   | Và       |
    | `or`    | Hoặc     |
    | `not`   | Phủ định |

   e. Toán tử thành viên
    | Toán tử  | Ý nghĩa        |
    | -------- | -------------- |
    | `in`     | Có trong       |
    | `not in` | Không có trong |

   f. Toán tử định danh
    | Toán tử  | Ý nghĩa        |
    | -------- | -------------- |
    | `is`     | Cùng đối tượng |
    | `is not` | Khác đối tượng |

   g. Toán tử trên bit
    | Toán tử | Ý nghĩa   |        |
    | ------- | --------- | ------ |
    | `&`     | AND bit   |        |
    | `       | `         | OR bit |
    | `^`     | XOR bit   |        |
    | `~`     | NOT bit   |        |
    | `<<`    | Dịch trái |        |
    | `>>`    | Dịch phải |        |
____________________________________________________________________________________________________________
   TỔNG HỢP 
    | Nhóm toán tử | Các toán tử                               
    | ------------ | ----------------------------------------------- 
    | Số học       | `+`, `-`, `*`, `/`, `//`, `%`, `**`             
    | So sánh      | `==`, `!=`, `>`, `<`, `>=`, `<=`                
    | Gán          | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` 
    | Logic        | `and`, `or`, `not`                             
    | Thành viên   | `in`, `not in`                                  
    | Định danh    | `is`, `is not`                                  
    | Trên bit     | `&`, `                                          



   2.3. Mệnh đề điều kiện và vòng lặp trong Python
     I. Mệnh đề điều kiện (Conditional Statements)
     1. Khái niệm
Trong lập trình, "mệnh đề điều kiện" dùng để "kiểm tra một điều kiện và quyết định chương trình sẽ thực hiện khối lệnh nào".
Điều kiện luôn cho kết quả:
* `True` (Đúng)
* `False` (Sai)
     2. Câu lệnh `if`
### Cú pháp
if điều_kiện:
    câu_lệnh
**Lưu ý:**
* Sau `if` phải có dấu `:`.
### Ví dụ
age = 20
if age >= 18:
    print("Bạn đã đủ tuổi.")
```

## 3. Câu lệnh `if...else`
Dùng khi có **2 trường hợp**.

### Cú pháp
if điều_kiện:
    câu_lệnh_1
else:
    câu_lệnh_2

### Ví dụ
age = 16
if age >= 18:
    print("Đủ tuổi")
else:
    print("Chưa đủ tuổi")

## 4. Câu lệnh `if...elif...else`
Dùng khi có **nhiều điều kiện**.

### Cú pháp
if điều_kiện_1:
    câu_lệnh

elif điều_kiện_2:
    câu_lệnh

elif điều_kiện_3:
    câu_lệnh

else:
    câu_lệnh

### Ví dụ
score = 8.5
if score >= 9:
    print("Xuất sắc")

elif score >= 8:
    print("Giỏi")

elif score >= 6.5:
    print("Khá")

else:
    print("Trung bình")

## 5. Điều kiện lồng nhau
Có thể đặt `if` bên trong `if`.

Ví dụ
age = 20
hasID = True
if age >= 18:
    if hasID:
        print("Được vào")

# II. Vòng lặp (Loops)
Vòng lặp dùng để **lặp đi lặp lại một hoặc nhiều câu lệnh**.

# 2. Vòng lặp `for`
`for` dùng để lặp qua một dãy giá trị hoặc các phần tử của một tập dữ liệu.

### Cú pháp
for biến in dãy_giá_trị:
    câu_lệnh

## Ví dụ 1
for i in range(5):
    print(i)

## Hàm `range()`
`range()` tạo ra một dãy số.

### Cú pháp
range(stop)

### Cú pháp
range(start, stop)

Ví dụ
for i in range(1,6):
    print(i)

### Cú pháp
range(start, stop, step)

Ví dụ
for i in range(2,11,2):
    print(i)

## Lặp qua List
fruits = ["Táo","Cam","Xoài"]
for fruit in fruits:
    print(fruit)

# 3. Vòng lặp `while`
`while` lặp khi điều kiện còn đúng.

### Cú pháp
while điều_kiện:
    câu_lệnh

## Ví dụ
i = 1
while i <= 5:
    print(i)
    i += 1

## Ví dụ tính tổng
tong = 0
i = 1
while i <= 5:
    tong += i
    i += 1
print(tong)

# III. Các câu lệnh điều khiển vòng lặp
## 1. `break`
`break` dùng để **thoát khỏi vòng lặp ngay lập tức**.

### Ví dụ
for i in range(1,10):
    if i == 5:
        break
    print(i)

## 2. `continue`
`continue` dùng để **bỏ qua lần lặp hiện tại và chuyển sang lần lặp tiếp theo**.

### Ví dụ
for i in range(1,6):
    if i == 3:
        continue
    print(i)

## 3. `pass`
`pass` là câu lệnh **không làm gì cả**, thường dùng làm chỗ giữ chỗ khi chưa viết mã.

### Ví dụ
if True:
    pass
print("Hello")


# IV. So sánh `for` và `while`
| Tiêu chí           | `for`                        | `while`                         |
| ------------------ | ---------------------------- | ------------------------------- |
| Điều kiện lặp      | Theo số lần hoặc tập dữ liệu | Theo điều kiện                  |
| Khi nào dùng       | Biết trước số lần lặp        | Không biết trước số lần lặp     |
| Nguy cơ lặp vô hạn | Thấp                         | Cao nếu quên cập nhật điều kiện |

# V. Ví dụ tổng hợp
n = 10
if n % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
for i in range(1,6):
    print(i)

x = 1
while x <= 3:
    print("Python")
    x += 1


# VI. Tóm tắt kiến thức
### Mệnh đề điều kiện
| Câu lệnh           | Chức năng              |
| ------------------ | ---------------------- |
| `if`               | Kiểm tra một điều kiện |
| `if...else`        | Hai trường hợp         |
| `if...elif...else` | Nhiều trường hợp       |

### Vòng lặp
| Vòng lặp | Chức năng                            |
| -------- | ------------------------------------ |
| `for`    | Lặp theo số lần hoặc qua tập dữ liệu |
| `while`  | Lặp khi điều kiện còn đúng           |

### Điều khiển vòng lặp
| Câu lệnh   | Ý nghĩa                       |
| ---------- | ----------------------------- |
| `break`    | Thoát khỏi vòng lặp           |
| `continue` | Bỏ qua lần lặp hiện tại       |
| `pass`     | Không thực hiện hành động nào |
