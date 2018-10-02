from entity import Printer
from entity import MFD
from entity import ParentClass
from entity import Child1
from entity import Child2
from random import randint

printer = Printer.Printer(20)

printer.set_name('Cyocera')

print(printer.get_name())

printer.do_print(6)

mfd = MFD.MFD(7)

mfd.set_name('HP')

print(mfd.get_name())

mfd.do_scan()

mfd.do_copy(8)

print('---------------------End of tasks 1-3---------------------')
print('--------------Beginning of the next task------------------')

arr = []

for i in range(10):
    arr.append(randint(1,2))
    if arr[i] == 1:
        arr[i] = Child1.Child1()
    else:
        arr[i] = Child2.Child2()

    arr[i].foo()


arr = [1, 2, 3, 4, 5]

try:
    print(arr[100])
except IndexError:
    print('Index out of range!')

try:
    print(noname)
except NameError:
    print('Undefined name')


try:
    val = int('Hello!')
except ValueError:
    print('Wrong type!')