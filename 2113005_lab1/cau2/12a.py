arr = int(input('nhap mang bat dau tu: '))
n = int(input('den: '))
for i in range(arr, n):
    if i % 2 != 0 and i % 5 != 0:
        print(i)
