#k) Đếm số lần xuất hiện của một số trong danh sách
def taomang(n):
    for i in range(n):
        nhapmang = int(input('phan tu thu{} cua mang'.format(i+1)))
        arr.append(nhapmang)
    return(arr)
def demsolanxuathien(n):
    for i in arr:
        xuathien = int(input('tim so xuat hien: '))
        cout = arr.count(xuathien)
        return cout
arr = []
number = int(input('nhap so phan tu cua mang'))
print(taomang(number),'so lan xuat hien la: ',demsolanxuathien(arr),'lan')