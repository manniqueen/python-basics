n = int(input())
counter = 0
min_number = 1000000

while counter < n:
    number = int(input())
    counter += 1
    if number < min_number:
        min_number = number

print(min_number)