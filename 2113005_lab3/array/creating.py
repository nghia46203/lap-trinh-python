# Nhập mô-đun "array" để tạo mảng
import array as arr

# Tạo một mảng có kiểu dữ liệu là số nguyên
a = arr.array('i', [1, 2, 3])

# In ra mảng gốc
print("Mảng mới được tạo là: ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# Tạo một mảng có kiểu dữ liệu là số thực
b = arr.array('d', [2.5, 3.2, 3.3])

# In ra mảng gốc
print("Mảng mới được tạo là: ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
