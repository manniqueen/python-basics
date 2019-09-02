budget = float(input())
extras = int(input())
outfit = float(input())
money_extras = extras * outfit

decor = budget * 0.1
sum = 0

if extras > 150:
    sum = (money_extras - (money_extras * 0.1) + decor)
else:
    sum = money_extras + decor

if sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {sum - budget:.2f} leva more.")
elif sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - sum:.2f} leva left.")