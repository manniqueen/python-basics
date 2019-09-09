age = int(input())
washing_machine = float(input())
toys_price = int(input())

saved_in_odd_years = 0
multiplier = 0
toys_in_even_years = 0

for year in range (1,age + 1):
    if year % 2 ==0:
        multiplier += 1
        saved_in_odd_years += 10 * multiplier
        saved_in_odd_years -= 1
    else:
        toys_in_even_years += 1

total_saved = saved_in_odd_years + (toys_in_even_years * toys_price)
diff = total_saved - washing_machine

if diff >= 0:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {abs(diff):.2f}')