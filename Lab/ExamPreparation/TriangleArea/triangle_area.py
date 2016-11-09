import math

side_a = input()
side_b = input()
side_c = input()

try:
    a = float(side_a)
    b = float(side_b)
    c = float(side_c)

    sides_are_more_than_zero = a > 0 and b > 0 and c > 0
    sides_form_triangle = a + b > c and a + c > b and b + c > a

    if sides_are_more_than_zero and  sides_form_triangle:
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("{:.2f}".format(s))
    else:
        print('INVALID INPUT')

except:
    print('INVALID INPUT')

