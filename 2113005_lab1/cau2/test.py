
def taomang(n):
    for i in range(n):
        nhapmang = input('nhap mang: ')
        arr.append(nhapmang)
        nguoc = list(reversed(arr))
    return nguoc     
nhap = int(input('nhap so luong mang: '))
arr = []
print(taomang(nhap))
