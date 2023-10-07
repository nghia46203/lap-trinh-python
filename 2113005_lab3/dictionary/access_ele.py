# Tạo một từ điển (Dictionary)
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Truy cập một phần tử bằng cách sử dụng khóa (key)
print("Truy cập phần tử bằng khóa:")
print(Dict['name'])

# Truy cập một phần tử bằng cách sử dụng khóa (key)
print("Truy cập phần tử bằng khóa:")
print(Dict[1])

# Truy cập một phần tử bằng cách sử dụng phương thức get()
print("Truy cập phần tử bằng cách sử dụng get:")
print(Dict.get(3))

# Tạo một từ điển (Dictionary)
Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
  
# Truy cập phần tử bằng cách sử dụng khóa (key)
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
