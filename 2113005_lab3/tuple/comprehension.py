from itertools import chain, product

# Khởi tạo các tuple
test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

# In ra các tuple gốc
print("Tuple gốc 1 : " + str(test_tuple1))
print("Tuple gốc 2 : " + str(test_tuple2))

# Tất cả các cặp kết hợp của 2 tuple
# Sử dụng chain() + product()
res = list(chain(product(test_tuple1, test_tuple2), product(test_tuple2, test_tuple1)))

# In ra kết quả
print("Tuple kết quả : " + str(res))
