month = input()
nights_count = int(input())

studio = None
apartment = None

if month == 'May' or month == 'October':
    studio = nights_count * 50
    apartment = nights_count * 65

    if nights_count > 7 and nights_count <= 14:
        studio -= studio * 0.05
    elif nights_count > 14:
        studio -= studio * 0.30
        apartment -= apartment * 0.1
elif month == 'June' or month == 'September':
    studio = nights_count * 75.2
    apartment = nights_count * 68.7

    if nights_count > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
elif month == 'July' or month == 'August':
    studio = nights_count * 76
    apartment = nights_count * 77

    if nights_count > 14:
        apartment -= apartment * 0.1

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
