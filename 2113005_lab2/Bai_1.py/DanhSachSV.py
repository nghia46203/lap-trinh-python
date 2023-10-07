from sinhvien import SinhVien
import datetime

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    def xuat(self):
        for sv in self.dssv:
            print(sv)
#tim sv theo mssv, neu co tra ve sinh vien
    def timsv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i]._maSo == mssv:
                return i
        else:
            return -1

# xóa sv có mssv, thong bao xoa đươc hoặc không
    def XoaSV(self, maSo: int) ->bool:
        vt = self.timVTsvtheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
# tim sv ten nam
    def timtensv(self, hoten: str):
         for i in range(len(self.dssv)):
            if self.dssv[i].hoten.lower('nguyen van a') == hoten.lower():
                return i
            return -1
#tim nhung sv sinh trước ngày 15/6/2000
    def timsinhviensinhtruocngay(self,sv: SinhVien ,ngaySinh:datetime,ngay):
        sinhvientimthay = []
        for i in self.dssv:
            if sv.ngaySinh < ngay:
                sinhvientimthay.append(sv)
        return sinhvientimthay
    
    
 