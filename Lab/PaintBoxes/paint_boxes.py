import math

width = float(input())
high = float(input())
one_box_covers = 1.76 #m2

area = width * high
result = area / one_box_covers
print(math.ceil(result))
