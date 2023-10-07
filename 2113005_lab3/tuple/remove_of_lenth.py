# Khởi tạo danh sách
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# In danh sách gốc
print("Danh sách gốc : " + str(test_list))

# Khởi tạo K
K = 1

# filter() lọc ra các giá trị không có độ dài bằng K và trả về kết quả
res = list(filter(lambda x : len(x) != K, test_list))

# In kết quả
print("Danh sách đã lọc : " + str(res))
