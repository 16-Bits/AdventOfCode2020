def main():
    data = open('advent1.txt', 'r')
    intList = []
    int1 = 0
    int2 = 0
    int3 = 0
    for line in data:
        number = int(line)
        intList.append(number)
    for item in intList:#ugly but it works
        int1 = item
        for item in intList:
            int2 = item
            for item in intList:
                int3 = item
                numsum = int1+int2+int3
                if numsum==2020:
                    print(int1*int2*int3)
                    print("epic win")
                    exit()
    print("epic fail")
if __name__ == '__main__':
    main()