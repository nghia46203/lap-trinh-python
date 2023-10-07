#i) Xuất tất cả các số lớn thứ nhì của danh sách
#lọc danh sách dảm dần in ra vị trí thứ 2
arr = []
def taodanhsach(n):
    for i in range(n):
        mang = input('nhap mang: ')
        arr.append(mang)
    return arr
def timsolonthu2(n):
    arr.sort(reverse=True)
    thu2 = arr[1]
    return thu2
num = int(input('nhap cac phan tu: '))
print(taodanhsach(num))
print('so lon thu 2: ',timsolonthu2(arr))