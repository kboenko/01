from entity import Printer
from entity import MFD

printer = Printer.Printer(20)

printer.set_name('Cyocera')

print(printer.get_name())

printer.do_print(6)

mfd = MFD.MFD(7)

mfd.set_name('HP')

print(mfd.get_name())

mfd.do_scan()

mfd.do_copy(8)

