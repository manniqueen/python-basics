import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = (math.fabs(x1 - x2))
width = (math.fabs(y1 - y2))
area = length * width
perimeter = 2 * (length + width)
print('%.2f' % area)
print('%.2f' % perimeter)