test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# In ra Tuple gốc
print("Tuple gốc : " + str(test_tuple))

# Làm phẳng Tuple chứa danh sách thành Tuple
res = []
for i in test_tuple:
    res.extend(i)
res = tuple(res)

# In ra kết quả
print("Tuple đã làm phẳng : " + str(res))
