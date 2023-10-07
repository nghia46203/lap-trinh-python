import math

def sum_square_root(n):
    total = 0
    for i in range(1, n + 1):
        total += math.sqrt(i)
    return total
number = 5
result = sum_square_root(number)
print("Tổng căn bậc hai của", number, "số nguyên đầu tiên là", result)