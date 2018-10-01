class Printer:

    __name = ''
    __number = 0

    def __init__(self, number):
        self.__number = number

    def set_name(self, name):
        self.__name = name + str(self.__number)

    def get_name(self):
        return self.__name

    def do_print(self, sheets_qty):
        for sheet in range(sheets_qty):
            print('Sheet ' + str(sheet + 1) + ' has printed!')