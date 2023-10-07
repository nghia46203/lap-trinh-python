from itertools import chain

# Khởi tạo danh sách
test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

# In danh sách gốc
print("Danh sách gốc : " + str(test_list))

# Trích xuất các chữ số từ danh sách Tuple
# Sử dụng map() + chain.from_iterable() + set() + vòng lặp
temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
	for ele in sub:
		res.add(ele)

# In kết quả
print("Các chữ số được trích xuất : " + str(res))
