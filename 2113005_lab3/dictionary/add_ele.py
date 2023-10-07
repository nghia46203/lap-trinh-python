# Tạo một từ điển (Dictionary) trống
Dict = {}
print("Từ điển trống: ")
print(Dict)

# Thêm các phần tử một cách từng phần tử một
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nTừ điển sau khi thêm 3 phần tử: ")
print(Dict)

# Thêm một tập hợp các giá trị
# vào một Khóa duy nhất
Dict['Value_set'] = 2, 3, 4
print("\nTừ điển sau khi thêm 3 phần tử: ")
print(Dict)

# Cập nhật giá trị cho Khóa đã tồn tại
Dict[2] = 'Welcome'
print("\nGiá trị của Khóa đã được cập nhật: ")
print(Dict)

# Thêm một Khóa con có giá trị vào Từ điển
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nThêm một Khóa con: ")
print(Dict)
