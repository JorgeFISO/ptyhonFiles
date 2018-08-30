def sortList(intList):
    print(intList)
    for i in range(1, len(intList)):
        move = i
        insert = intList[i]
        while((move > 0) and (intList[move - 1] > insert)):
            intList[ i ] = intList[ i - 1]
            move -= 1

        intList[ move] = insert

    print(intList)



numberList = [34, 56, 4, 10, 77, 51, 93, 30, 5, 52]

sortList(numberList)