def fibonacci_khongdequy(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibo = [0, 1]
        for i in range(2, n):
            fibo.append(fibo[i - 1] + fibo[i - 2])
        return fibo[n - 1]

n = int(input("Nhập số Fibonacci cần tìm: "))
result = fibonacci_khongdequy(n)
if result is not None:
    print("Số Fibonacci thứ", n, "là", result)
else:
    print("Vui lòng nhập một số nguyên dương.")
