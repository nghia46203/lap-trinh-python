# Tạo một Tập hợp (Set)
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Tập hợp ban đầu: ")
print(set1)
 
# Xóa các phần tử khỏi Tập hợp
# bằng cách sử dụng phương thức Remove()
set1.remove(5)
set1.remove(6)
print("\nTập hợp sau khi xóa hai phần tử: ")
print(set1)
 
# Xóa các phần tử khỏi Tập hợp
# bằng cách sử dụng phương thức Discard()
set1.discard(8)
set1.discard(9)
print("\nTập hợp sau khi bỏ đi hai phần tử: ")
print(set1)
 
# Xóa các phần tử khỏi Tập hợp
# bằng cách sử dụng vòng lặp
for i in range(1, 5):
    set1.remove(i)
print("\nTập hợp sau khi xóa một loạt các phần tử: ")
print(set1)

# Xóa một phần tử bằng phương thức pop()
set1.pop()
print("\nTập hợp sau khi loại bỏ một phần tử: ")
print(set1)

# Xóa tất cả các phần tử bằng phương thức clear()
set1.clear()
print("\nTập hợp sau khi xóa tất cả các phần tử: ")
print(set1)
