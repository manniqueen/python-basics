n = int(input())
counter = 0
max_number = -1000000

while counter < n:
    number = int(input())
    counter += 1
    if number > max_number:
        max_number = number

print(max_number)