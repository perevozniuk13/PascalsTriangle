def pascalsTriangle(n):
    first = [1]
    if n == 1:
        print(first)
        return "Done!"
    second = [1, 2, 1]
    if n == 2:
        print(first)
        print(second)
        return "Done!"
    currentRow = second
    print(first)
    print(second)
    for i in range(2, n+1):
        nextRow = [1]
        for j in range(len(currentRow)-1):
            nextRow.append(currentRow[j]+currentRow[j+1])
        nextRow.append(1)
        print(nextRow)
        currentRow = nextRow
    return "Done!"

print(pascalsTriangle(int(input("Type in the number of rows in Pascal`s triangle:"))))