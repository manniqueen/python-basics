name = input()
counter = 1
marks_sum = 0
exclusions = 0
is_excluded = False

while counter <= 12:
    mark = float(input())
    if mark >= 4.00:
        marks_sum += mark
        counter += 1
    else:
        exclusions += 1

    if exclusions >= 2:
        is_excluded = True
        break

if is_excluded:
    print(f'{name} has been excluded at {counter} grade')
else:
    average_mark = marks_sum / 12
    print(f'{name} graduated. Average grade: {average_mark:.2f}')