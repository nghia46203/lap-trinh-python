def tu_dien():

    # Khai báo hàm băm
    key_value = {}

    # Khởi tạo các giá trị
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value", key_value)

    print("Nhiệm vụ 2:-\nKhóa và Giá trị được sắp xếp",
          "theo thứ tự alphabet theo khóa")

    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


def main():
    # Gọi hàm
    tu_dien()


# Gọi hàm main
if __name__ == "__main__":
    main()
