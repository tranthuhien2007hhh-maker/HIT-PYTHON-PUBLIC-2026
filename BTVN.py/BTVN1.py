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
