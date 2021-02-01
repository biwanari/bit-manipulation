import math

class BinaryClass:

    def __init__(self):
        self.data = None

    def setData(self, value):
        self.data = value
    
    @staticmethod
    def getData(self):
        return self.data

    def fromIntToBin(self, integer_data):
        valueBin = []
        value = self.data
        if value == 0:
            return 0
        else:
            while value > 0:
                valueBin.append(value % 2)
                value = value // 2
            valueBin.reverse()
            return valueBin

    
    def fromFloatToBin(self, floating_data):
        pass

    def twosComplement(self, data):

if __name__ == "__main__":
    pass