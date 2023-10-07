# Nhập mô-đun "array"
import array

# Khởi tạo mảng với các giá trị
# Khởi tạo mảng với số nguyên có dấu
arr = array.array('i', [1, 2, 3, 1, 2, 5])

# In ra mảng gốc
print ("Mảng mới được tạo là : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")

print ("\r")

# Sử dụng index() để in ra vị trí của lần xuất hiện đầu tiên của số 2
print ("Vị trí của lần xuất hiện đầu tiên của số 2 là : ", end ="")
print (arr.index(2))

# Sử dụng index() để in ra vị trí của lần xuất hiện đầu tiên của số 1
print ("Vị trí của lần xuất hiện đầu tiên của số 1 là : ", end ="")
print (arr.index(1))
