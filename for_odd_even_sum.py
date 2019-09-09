odd_sum = 0
even_sum = 0

n = int(input())

for i in range (1, n + 1):
    num = int (input())

    if i % 2 == 0:
        odd_sum += num
    else:
        even_sum += num

if even_sum == odd_sum:
    print("Yes")
    print(f'Sum = {odd_sum}')
else:
    difference = abs(odd_sum - even_sum)
    print(f'No')
    print(f'Diff = {difference}')