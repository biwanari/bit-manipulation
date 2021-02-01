def fromIntToBin(data):
    valueBin = []
    value = data
    if value == 0:
        return 0
    else:
        while value > 0:
            valueBin.append(value % 2)
            value = value // 2
        valueBin.reverse()
        return valueBin


if __name__ == "__main__":
    x = [x for x in range(0, 257)]
    for i in range(len(x)):
        print(f"{x[i]}  : {str(fromIntToBin(x[i]))}")