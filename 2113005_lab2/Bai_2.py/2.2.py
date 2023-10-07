#tang giam ho ten
def readFile(n):
    file = open('sinhvien.txt')
    kq = file.read()
    file.close()
    return kq


def giamtheohoten(n):
    docfile = readFile('sinhvien.txt')   
    names = [name.strip() for name in docfile]
    sorted_names = sorted(names, reverse=True)
    for name in sorted_names:
        print(name)
    return name
print(readFile('sinhvien.txt'))
print(giamtheohoten())