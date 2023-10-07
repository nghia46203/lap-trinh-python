
# nhập 'array' để tạo mảng"
import array as arr

# "Mảng với kiểu int"
a = arr.array('i', [1, 2, 3])


print ("Mảng trước khi chèn phần tử : ", end =" ")
for i in range (0, 3):
	print (a[i], end =" ")
print()

# Chèn mảng bằng cách sử dụng hàm # insert()
# insert() function
a.insert(1, 4)

print ("Mảng trước khi chèn phần tử : ", end =" ")
for i in (a):
	print (i, end =" ")
print()

# Mảng với kiểu float
b = arr.array('d', [2.5, 3.2, 3.3])

print ("Mảng trước khi chèn phần tử : ", end =" ")
for i in range (0, 3):
	print (b[i], end =" ")
print()

# Thêm một phần tử bằng cách sử dụng hàm append()"
b.append(4.4)

print ("Mảng trước khi chèn phần tử : ", end =" ")
for i in (b):
	print (i, end =" ")
print()
