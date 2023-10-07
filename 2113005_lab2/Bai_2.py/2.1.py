# Mở tập tin
file_path = 'sinhvien.txt'
file = open(file_path, 'r')
content = file.read()
file.close()
print(content)