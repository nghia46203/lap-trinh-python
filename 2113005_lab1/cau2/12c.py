num  = int(input('nhap phan tu:'))
arr = []
def mang(n):
    for i in range(n):
        element = input('nhap phan tu {} phan tu: '.format(i+1))
        arr.append(element)
    return(arr)
def maxgiatri(arr):
    maxlavue = max(arr)  
    return maxlavue   
print(mang(num))
print('phan tu lon nhat: ',maxgiatri(arr))