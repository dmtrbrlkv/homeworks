class Printer():
    def log(self, *values):
        print(values)


class FormattedPrinter(Printer):
    def log(self, *values):
        print("*" * 10)
        Printer.log(self, *values)
        print("*" * 10)



fp = FormattedPrinter()
fp.log(1, 2 ,3, "12312")