type = input()
r = int(input())
c = int(input())

total_chairs = r * c
price = None

if type == 'Premiere':
    price = total_chairs * 12
elif type == 'Normal':
    price = total_chairs * 7.5
elif type == 'Discount':
    price = total_chairs * 5

if price:
    print(f'{price:.2f} leva')