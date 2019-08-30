import math
figure_type = input()


if figure_type == 'square':
    side = float(input())
    area = side * side
    print('%.3f' % area)
elif figure_type == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print('%.3f' % area)
elif figure_type == 'circle':
    r = float(input())
    area = math.pi * r * r
    print('%.3f' % area)
elif figure_type == 'triangle':
    a = float(input())
    h = float(input())
    area = a * h / 2
    print('%.3f' % area)

