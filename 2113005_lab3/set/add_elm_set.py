# Chương trình Python để thể hiện
# Thêm các phần tử vào một Tập hợp

# Tạo một Tập hợp (Set)
set1 = set()
print("Tập hợp ban đầu rỗng: ")
print(set1)

# Thêm phần tử và tuple vào Tập hợp
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nTập hợp sau khi thêm ba phần tử: ")
print(set1)

# Thêm các phần tử vào Tập hợp
# bằng cách sử dụng Iterator
for i in range(1, 6):
	set1.add(i)
print("\nTập hợp sau khi thêm các phần tử từ 1-5: ")
print(set1)

# Sử dụng hàm Update
set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nTập hợp sau khi thêm các phần tử bằng cách sử dụng Update: ")
print(set1)
