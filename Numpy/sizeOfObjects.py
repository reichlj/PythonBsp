import sys
lst = [24, 12, 57]
size_of_list_object = sys.getsizeof(lst)   # only green box
size_of_elements = len(lst) * sys.getsizeof(lst[0]) # 24, 12, 57
total_list_size = size_of_list_object + size_of_elements
print("Größe ohne Größe der Elemente: ", size_of_list_object)
print("Größe aller Elemente: ", size_of_elements)
print("Gesamtgröße der Liste: ", total_list_size)


x = int()
print("Größe von int-Object int()", sys.getsizeof(x))
x = 42
print("Größe von int-Object int(42)", sys.getsizeof(x))
x = 1234567890
print("Größe von int-Object int(1234567890)", sys.getsizeof(x))
x = 12345678901234567890
print("Größe von int-Object int(12345678901234567890)", sys.getsizeof(x))

y = float()
print("Größe von float-Object float()", sys.getsizeof(y))
print("y=", y)
y = float(12.34)
print("Größe von float-Object float(12.34)", sys.getsizeof(y))
print("y=", y)
y = float(124567.1234567890)
print("Größe von float-Object float(124567.1234567890)", sys.getsizeof(y))
print("y=", y)
y = float(12456789012345.123456789012345)
print("Größe von float-Object float(12456789012345.123456789012345)", sys.getsizeof(y))
print("y=", y)
print("id(x)=", id(x))
