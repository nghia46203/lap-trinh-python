import math

def giaithua(n):
    kq = 1
    for i in range(1, n+1):
        kq *= i
    return(kq)
num = int(input('nhap num: '))
result =giaithua(num)
print('giai thua cua',num,'là',result)