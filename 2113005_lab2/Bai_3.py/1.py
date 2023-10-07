class PhanSo:
    def __init__(self, tu=0, mau=1):
         self.tu = tu
         self.mau = mau
    def __rutGon__(self):
        pass
    def __add__(self, other):
        tu = (self.tu*other.mau+self.mau*other.tu)/self.mau*other.mau
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __truediv__(self,other):
       pass
    def __str__(self):
        return f"{self.tu}/{self.mau}"

a = PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3, 5)
print(f"{a} + {b} = {a + b}")
print(f'{a} - {b} = {a - b}')
print(f"{a} * {b} = {a * b}")
print(f'{a} / {b} = {a / b}')