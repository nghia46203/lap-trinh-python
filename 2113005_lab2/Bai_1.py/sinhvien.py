import datetime

class SinhVien:
    #BIẾN CỦA LỚP
    truong = 'ĐẠI HỌC ĐÀ LẠT'
#ham khoi tao,ham tao lap
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime ) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
# cho phép truy xuất tới thuộc tính từ bên ngoài thông qua trường maSo
    @property
    def maSo(self):
        return self._maSo
#
    @staticmethod
    def LaMaSoHopLe(maso: int):
        return len(str(maso))==7
# phương thức của lớp chỉ truy xuất tới các biến thành viên của lớp
# không truy xuất được các thuộc tính riêng của dối tượng
    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
# thay doi gia tri thuoc tinh maSo
    @maSo.setter
    def maSo(self, maso):
        if self.LaMaSoHopLe(maso):
            self._maSo = maso
# ghi de phuong thuc tostring
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
# hanh vi cua doi tuong tostring
    def xuat(self):
        print(f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}")

