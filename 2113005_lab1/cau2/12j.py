def taomang(n):
    for i in range(n):
        nhapmang = input('nhap mang')
        arr.append(nhapmang)
    return arr
def tongmang(n):
    intt = list(map(int, arr))
    tong = sum(intt)
    return tong
arr = []
number = int(input('nhap mang: '))
print(taomang(number),'có tổng là: ',tongmang(arr))