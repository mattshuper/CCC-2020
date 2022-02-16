# The first line of input contains the number of drops of paint, N, where 2  N  100 and N is an
# integer. Each of the next N lines contain exactly two positive integers X and Y separated by one
# comma (no spaces). Each of these pairs of integers represents the coordinates of a drop of paint on
# the canvas. Assume that X < 100 and Y < 100, and that there will be at least two distinct points.
# The coordinates (0, 0) represent the bottom-left corner of the canvas.
# For 12 of the 15 available marks, X and Y will both be two-digit integers.

numDrops = int(input())
cords = input()
splitCords = cords.split(',')
splitCords = [int(n) for n in splitCords]
maxX = splitCords[0]
minX = splitCords[0]
maxY = splitCords[1]
minY = splitCords[1]
for x in range(0,numDrops-1):
    cords = input()
    splitCords = cords.split(',')
    splitCords = [int(n) for n in splitCords]
    if splitCords[0] > maxX:
        maxX = splitCords[0]
    if splitCords[0] < minX:
        minX = splitCords[0]
    if splitCords[1] > maxY:
        maxY = splitCords[1]
    if splitCords[1] < minY:
        minY = splitCords[1]
maxX += 1
maxY += 1
minX -= 1
minY -= 1
print(f"{minX},{minY}")
print(f"{maxX},{maxY}")


