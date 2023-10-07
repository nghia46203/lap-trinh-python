#l) Xuất các số xuất hiện n lần trong danh sách
arr = []
def taomang(n):
    for i in range(n):
        mang = int(input('nhap mang: '))
        arr.append(mang)
    return(arr)
def xuatso(n):
    for i in arr:
        kq = arr.count(num)
    return kq

num = int(input('nhap so can tim: '))
number = int(input('nhap so mang: '))
print(f'',taomang(number),'so:',num,'so lan xuat hien', xuatso(arr),'lan')