import sys
from num_thai.thainumbers import NumThai

num = NumThai()
max = sys.maxsize
min = -sys.maxsize-1

#9223372036854771
n = num.NumberToTextThai(-1111111111111111)



print(max,min)

print(n)


