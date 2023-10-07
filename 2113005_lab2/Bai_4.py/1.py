
class TaoMang:
    def __init__(self,num ):
        self.num=num
    def GoiMang(self):
        for i in self.num:
            print(i)
   

class PhanSo(TaoMang):
    def xuat_am(self):
        return [i for i in self.num if i<0]
    def __TimSoDuongNhoNhat__(self):
      nhonhat = None
      for i in self.num:
          if i > 0 and (nhonhat is None or i < nhonhat):
            nhonhat = i
            return i
    def TimVtriX (self, x:int):
            for i in self.num:
                if i in self.num:
                    return self.num.index(x)
            return -1
            
    def __TongAllSoAm__(self):
        soam = []
        for i in self.num:
            if i < 0:
                soam.append(i)
        tong = sum(soam)
        return tong

    def XoaPhanSoX(self, x: int) :
        for i in self.num:
            if x in self.num:
                self.num.remove(x)
                return 1
            print("Đã xóa phần tử khỏi danh sách:")
            PhanSo.GoiMang(taoMang)
        return 0

taoMang = TaoMang([-1, 2,-3, 4, 5, 6])
taoMang.GoiMang()
print('1: xuất số âm: ',PhanSo.xuat_am(taoMang))
print('2: xuất số dương bé nhất:',PhanSo.__TimSoDuongNhoNhat__(taoMang))
kq=PhanSo.TimVtriX(taoMang,5)
print('3: vị trí của:',kq)
print('4: tong cua all so am: ', PhanSo.__TongAllSoAm__(taoMang))
kq = PhanSo.XoaPhanSoX(taoMang,2)
if kq == 1:
    print("Đã xóa phần tử{x} khỏi danh sách:")
    PhanSo.GoiMang(taoMang)
else:
    print("không có phần tử tương ứng:")
    PhanSo.GoiMang(taoMang)   
    

