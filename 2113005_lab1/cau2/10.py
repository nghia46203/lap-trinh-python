n = int(input("Nhập kích thước tam giác: "))

for i in range(n):
    for j in range(n):
        if(j==0 or j==i or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
