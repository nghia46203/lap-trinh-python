# Tạo một tập hợp (set)
set1 = set(["Geeks", "For", "Geeks"])
print("\nTập hợp ban đầu")
print(set1)
 
# Truy cập phần tử bằng
# vòng lặp for
print("\nCác phần tử của tập hợp: ")
for i in set1:
    print(i, end=" ")
 
# Kiểm tra sự tồn tại của phần tử
# bằng từ khóa 'in'
print("Geeks" in set1)
