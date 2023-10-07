# Tạo một Tuple
# với các kiểu dữ liệu kết hợp
Tuple1 = (5, 'Chào mừng', 7, 'Geeks')
print("\nTuple với các kiểu dữ liệu kết hợp: ")
print(Tuple1)

# Tạo một Tuple
# với các tuple lồng nhau
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple với các tuple lồng nhau: ")
print(Tuple3)

# Tạo một Tuple
# với sự lặp lại
Tuple1 = ('Geeks',) * 3
print("\nTuple với sự lặp lại: ")
print(Tuple1)

# Tạo một Tuple
# bằng cách sử dụng vòng lặp
Tuple1 = ('Geeks')
n = 5
print("\nTuple với một vòng lặp")
for i in range(int(n)):
	Tuple1 = (Tuple1,)
	print(Tuple1)
