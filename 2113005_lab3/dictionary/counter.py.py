from collections import Counter

def tinh_nguoi_chien_thang(danh_sach_phieu):
    phieu_bau = Counter(danh_sach_phieu)
    ket_qua = {}

    for so_lan_bau in phieu_bau.values():
        ket_qua[so_lan_bau] = []

    for (ung_vien, so_lan_bau) in phieu_bau.items():
        ket_qua[so_lan_bau].append(ung_vien)

    # Sắp xếp các khóa theo thứ tự giảm dần để lấy giá trị lớn nhất
    so_lan_bau_max = sorted(ket_qua.keys(), reverse=True)[0]
    if len(ket_qua[so_lan_bau_max]) > 1:
        print(sorted(ket_qua[so_lan_bau_max])[0])
    else:
        print(ket_qua[so_lan_bau_max][0])

# Chương trình chạy chính
if __name__ == "__main__":
    danh_sach_phieu = ['john', 'johnny', 'jackie', 'johnny',
                     'john', 'jackie', 'jamie', 'jamie',
                     'john', 'johnny', 'jamie', 'johnny',
                     'john']
    tinh_nguoi_chien_thang(danh_sach_phieu)
