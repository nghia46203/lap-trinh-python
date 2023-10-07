tuple1 = (5, 10, 6, 4, 8, 9)

print(str(tuple1))
k = 2

tuple1 = list(tuple1)
temp = sorted(tuple1)
res = tuple(temp[:k] + temp[-k:])

print("Phần tử nhỏ thứ nhất: " + str(res[0]))
print("Phần tử lớn thứ nhất: " + str(res[-1]))
