# Nhập mô-đun "array"
import array as arr

# Tạo một danh sách
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tạo mảng 'a' với kiểu dữ liệu số nguyên và sử dụng danh sách 'l'
a = arr.array('i', l)
print("Mảng ban đầu: ")
for i in (a):
	print(i, end =" ")

# In ra các phần tử trong một khoảng
# sử dụng phép cắt (Slice)
Sliced_array = a[3:8]
print("\nCắt phần tử trong khoảng từ 3-8: ")
print(Sliced_array)

# In ra các phần tử từ vị trí
# đã xác định trước đến cuối mảng
Sliced_array = a[5:]
print("\nCác phần tử cắt từ vị trí thứ 5 "
	"đến cuối mảng: ")
print(Sliced_array)

# In ra tất cả các phần tử từ
# đầu đến cuối mảng
Sliced_array = a[:]
print("\nIn ra tất cả phần tử sử dụng phép cắt: ")
print(Sliced_array)
