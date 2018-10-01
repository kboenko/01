from entity import Printer

class MFD(Printer.Printer):

    def do_scan(self):
        print('Page has been scanned!')

    def do_copy(self, copies_qty):
        for copy in range(copies_qty):
            print('Copy ' + str(copies_qty) + ' is ready!')