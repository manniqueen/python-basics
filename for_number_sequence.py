n = int(input())
min_num = 10000
max_num = -10000

for i in range(0,n):
    num = int(input())

    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')