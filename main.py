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

parent = ParentClass.Parent()
child1 = Child1.Child1()
child2 = Child2.Child2()
arr = []

case = {
    '1': Child1.Child1(),
    '2': Child2.Child2()
}

for i in range(10):
    arr.append(randint(1,2))
    if arr[i] == 1:
        arr[i] = case['1']
    else:
        arr[i] = case['2']

    arr[i].foo()