import math
length = float(input('the length of a rectangle:'))
width = float(input('the width of a rectangle:'))
area = length * width
perimeter = 2 * length + 2 * width
if length > 0 and width > 0:
    print("The area of the rectangle is:", area)
    print("The perimeter of the rectangle is:", perimeter)
else:
    (print("wrong numbers."))
