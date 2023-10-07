from collections import Counter

def taomang(n):
    for i in range(n):
        nhapmang = input('nhap mang')
        arr.append(nhapmang)
    return arr
def tongmang(n):
    counter = Counter(arr)
    max_count = max(counter.values())
    most_common_numbers = [num for num, count in counter.items() if count == max_count]
    return most_common_numbers
arr = []
number = int(input('nhap mang: '))
print(taomang(number),'mang xuat hien nhieu nhat là: ',tongmang(arr))

