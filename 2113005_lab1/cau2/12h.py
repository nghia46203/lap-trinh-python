# Đảo ngược trật tự các phần tử của danh sách
def taomang(n):
    for i in range(n):
        num = input('nhap mang'.format(i))
        arr.append(num)
    return arr
def daonguoc(n):
    nguoc = list(reversed(arr))
    return(nguoc)
arr = []
nhap = int(input('nhap cac phan tu: '))
print(taomang(nhap))
print(daonguoc(arr))