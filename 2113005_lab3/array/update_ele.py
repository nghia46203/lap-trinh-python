# Nhập mô-đun "array"
import array

# Khởi tạo mảng với các giá trị mảng
# Khởi tạo mảng với số nguyên có dấu
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# In ra mảng gốc
print ("Mảng trước khi cập nhật : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")

print ("\r")

# Cập nhật một phần tử trong mảng
arr[2] = 6
print("Mảng sau khi cập nhật : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
print()

# Cập nhật một phần tử trong mảng
arr[4] = 8
print("Mảng sau khi cập nhật : ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
