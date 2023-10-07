arr = []
def sole(n):
    for i in range(n):
        element = input('nhap so le thu {}: '.format(i+1))
        if i % 2 != 1:
            arr.append(element)
    return(arr)
def tong(arr):
    mang = list(map(int,arr))
    kq = sum(mang)
    return kq
num = int(input('nhap day so le: '))
print('danh sach cac so le: ',sole(num))
print('tong so le',tong(arr))
print(type(tong(arr)))