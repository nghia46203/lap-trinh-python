import math
def fibonacci(n):
    kq = int(math.sqrt(n))
    return kq * kq == n
def fibonaccinumber(x):
    return fibonacci(5*x*x+4) or fibonacci(5*x*x-4)
number = int(input('nhap so nguyen n: '))
if fibonacci(number):
    print(number,'là số fibonacci')
if fibonaccinumber(number):
    print(number,'không phải là số fibonacci')