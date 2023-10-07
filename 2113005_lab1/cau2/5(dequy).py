def fibonacci_dequy(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_dequy(n - 1) + fibonacci_dequy(n - 2)

n = int(input("Nhập số Fibonacci cần tìm: "))
result = fibonacci_dequy(n)
if result is not None:
    print("Số Fibonacci thứ", n, "là", result)
else:
    print("Vui lòng nhập một số nguyên dương.")