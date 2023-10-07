test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

# In ra tuple gốc
print("Tuple gốc : " + str(test_tuple))

# Khởi tạo các khóa (keys)
keys = ['khóa', 'giá trị', 'ID']

# Chuyển đổi Tuple lồng nhau thành từ điển tùy chỉnh với khóa
# Sử dụng zip() + list comprehension
res = [{key: val for key, val in zip(keys, sub)}
       for sub in test_tuple]

# In ra kết quả
print("Từ điển chuyển đổi : " + str(res))
