length = int(input('enter your num: '))
my_list = []
for _ in range(length):
    cout = int(input('nhap so'))
    my_list.append(cout)
find = my_list.count(4)
print(find)

