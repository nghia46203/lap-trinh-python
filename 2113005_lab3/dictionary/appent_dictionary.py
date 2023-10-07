test_dict = {"Gfg": 1, "is": 3, "Best": 2}

# In ra từ điển gốc
print("Từ điển ban đầu là : " + str(test_dict))

# Lấy danh sách các khóa (keys) và giá trị (values) từ từ điển
a = list(test_dict.keys())
b = list(test_dict.values())

# Kết hợp danh sách khóa và danh sách giá trị
a.extend(b)
res = a

# In ra kết quả
print("Danh sách khóa và giá trị theo thứ tự : " + str(res))
