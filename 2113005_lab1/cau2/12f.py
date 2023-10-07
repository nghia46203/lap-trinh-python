#) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng
#tạo mảng số lẻ và không chia hết cho 3
# nhân mảng

arr = []
def mangle(n):
    for i in range(n):
        element = input('nhap mang{}: '.format(i+1))
        if i % 2 != 0:
            arr.append(element)
    return arr
def nhanmang(arr):
    mang = list(map(int,arr))
    ket_qua = 1
    for phan_tu in mang:
        ket_qua *= phan_tu
    return ket_qua
num = int(input('nhap so phan tu: '))
print('danh sach cac so le',mangle(num))
print('tích các số lẻ trong mảng:',nhanmang(arr))
print(type(nhanmang(arr)))