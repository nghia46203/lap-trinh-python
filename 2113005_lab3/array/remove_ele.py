# Nhập mô-đun "array" để thực hiện các thao tác trên mảng
import array

# Khởi tạo mảng với các giá trị mảng
# Khởi tạo mảng với số nguyên có dấu
arr = array.array('i', [1, 2, 3, 1, 5])

# In ra mảng gốc
print("Mảng mới được tạo là: ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")

# Sử dụng pop() để loại bỏ phần tử ở vị trí thứ 2
print("Phần tử được loại bỏ là: ", end="")
print(arr.pop(2))

# In ra mảng sau khi loại bỏ
print("Mảng sau khi loại bỏ là: ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")

# Sử dụng remove() để loại bỏ lần xuất hiện đầu tiên của số 1
arr.remove(1)

# In ra mảng sau khi loại bỏ
print("Mảng sau khi loại bỏ là: ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")
