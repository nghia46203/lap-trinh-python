def SapXep_Tuple(tup):

	# reverse = None (Sắp xếp theo thứ tự tăng dần)
	# key được thiết lập để sắp xếp dựa trên phần tử thứ hai
	# của sublist sử dụng lambda
	tup.sort(key=lambda x: x[1])
	return tup

# Mã nguồn
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

# In ra danh sách các tuple đã sắp xếp
print(SapXep_Tuple(tup))
