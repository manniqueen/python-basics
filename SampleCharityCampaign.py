days = int(input())
cooks = int(input())
cakes_number = int(input())
waffles_number = int(input())
pancakes_number = int(input())

cakes_profit_by_one = cakes_number * 45
waffles_profit_by_one = waffles_number * 5.80
pancakes_profit_by_one = pancakes_number * 3.20

cakes_profit_by_all = cakes_profit_by_one * cooks
waffles_profit_by_all = waffles_profit_by_one * cooks
pancakes_profit_by_all = pancakes_profit_by_one * cooks

profitTotal = (cakes_profit_by_all + waffles_profit_by_all + pancakes_profit_by_all) * days
expenses = profitTotal / 8
profit_final = profitTotal - expenses

print('%.2f' % profit_final)


