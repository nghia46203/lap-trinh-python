from sinhvien import SinhVien
from DanhSachSV import DanhSachSv
from datetime import datetime

sv0 = SinhVien(2113005, "nguyen van b",datetime.strptime("04/6/2003","%d/%m/%Y"))
sv1 = SinhVien(2113006, "nguyen van a",datetime.strptime("08/7/2002","%d/%m/%Y"))

dssv = DanhSachSv()
dssv.themSinhVien(sv0)
dssv.themSinhVien(sv1)

dssv.xuat()

ms = 2113005
tim = dssv.timsv(ms)
print(f'sinh vien co ma so la: {ms} o vi tri thu {tim+1}')

