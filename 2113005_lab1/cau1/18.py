def sum_three(x, y, z):
     sum = x + y + z
     if   x == y == z:
          sum = sum*3
          return sum
print(sum_three(1, 2, 3))
print(sum_three(3,3,3))