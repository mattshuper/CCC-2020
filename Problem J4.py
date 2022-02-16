# The input will consist of exactly two lines containing only uppercase letters. The first line will be
# the text T, and the second line will be the string S. Each line will contain at most 1000 characters.
# For 6 of the 15 available marks, S will be exactly 3 characters in length.

text = input()
string = input()
cyclicShift = False


letters = [n for n in string]
cyclicShifts = []
cyclicShifts.append(string)

letters = [n for n in string]
for i in range(0,len(string)-1):
    shift = ""
    letters.append(letters[0])
    del letters[0]
    # print(letters)
    for element in letters:
        shift = shift + element
    cyclicShifts.append(shift)

# print(cyclicShifts)

for x in range(0,len(text)-len(string)):
    testSet = ""
    for i in range(0,len(string)):
        testSet = testSet + text[x+i]
    for element in cyclicShifts:
        if testSet == element:
            cyclicShift = True

if cyclicShift == True:
    print("yes")
else:
    print("no")
    
