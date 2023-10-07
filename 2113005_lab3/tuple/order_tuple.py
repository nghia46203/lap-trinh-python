test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

# In danh sách gốc
print("Danh sách gốc : " + str(test_list))

# Khởi tạo danh sách thứ tự
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

# Sắp xếp Tuple theo danh sách
# Sử dụng setdefault() + sorted() + lambda
temp = dict()
for key, ele in enumerate(ord_list):
	temp.setdefault(ele, []).append(key)	
res = sorted(test_list, key=lambda ele: temp[ele[0]].pop())

# In kết quả
print("Danh sách Tuple được sắp xếp : " + str(res))
