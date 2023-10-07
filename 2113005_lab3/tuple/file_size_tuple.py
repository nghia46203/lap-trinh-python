import sys 

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Sư tử"), ( 2, "Hổ"), (3, "Cáo"), (4, "Sói"))

print("Kích thước của Tuple1 sử dụng getsizeof: " + str(sys.getsizeof(Tuple1)) + "byte")

print("Kích thước của Tuple1 sử dụng __sizeof__: "+str(Tuple1.__sizeof__()) + "byte")
