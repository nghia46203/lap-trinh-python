# Một ví dụ minh họa về tất cả các phương thức của từ điển
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# Phương thức copy()
dict2 = dict1.copy()
print(dict2)

# Phương thức clear()
dict1.clear()
print(dict1)

# Phương thức get()
print(dict2.get(1))

# Phương thức items()
print(dict2.items())

# Phương thức keys()
print(dict2.keys())

# Phương thức pop()
dict2.pop(4)
print(dict2)

# Phương thức popitem()
dict2.popitem()
print(dict2)

# Phương thức update()
dict2.update({3: "Scala"})
print(dict2)

# Phương thức values()
print(dict2.values())
