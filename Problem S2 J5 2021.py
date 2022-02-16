# The first line of input will be a positive integer M. The second line of input will be a positive
# integer N. The third line of input will be a positive integer K. The remaining input will be
# K lines giving the choices made by the artist. Each of these lines will either be R followed
# by a single space and then an integer which is a row number, or C followed by a single space
# and then an integer which is a column number. Rows are numbered top down from 1 to M.
# Columns are numbered left to right from 1 to N.

numRows = int(input())
numColumns = int(input())
choices = int(input())

flippedRows = []
flippedColumns = []
flippedRowsCount = 0
flippedColumnsCount = 0

gold = 0

#switcheroni

for x in range(0,choices):
    flipped = False
    axisDesignation, rcNumber = [i for i in input().split()]
    rcNumber = int(rcNumber)
    if axisDesignation == "C":
        for element in flippedColumns:
            if rcNumber == element:
                flipped = True
        if flipped == True:
            gold = gold + flippedRowsCount - (numRows - flippedRowsCount)
            flippedColumns.remove(rcNumber)
            flippedColumnsCount -= 1
        if flipped == False:
            gold = gold - flippedRowsCount + (numRows - flippedRowsCount)
            flippedColumns.append(rcNumber)
            flippedColumnsCount += 1
    
    if axisDesignation == "R":
        for element in flippedRows:
            if rcNumber == element:
                flipped = True
        if flipped == True:
            gold = gold + flippedColumnsCount - (numColumns - flippedColumnsCount)
            flippedRows.remove(rcNumber)
            flippedRowsCount -= 1
        if flipped == False:
            gold = gold - flippedColumnsCount + (numColumns - flippedColumnsCount)
            flippedRows.append(rcNumber)
            flippedRowsCount += 1

print(gold)

