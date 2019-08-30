whiskey_price = float(input())
beer_litres = float(input())
wine_litres = float(input())
brandy_litres = float(input())
whiskey_litres = float(input())

brandy_price = whiskey_price * 0.5
wine_price = brandy_price * 0.6
beer_price = brandy_price * 0.2
final_expenses = (whiskey_price * whiskey_litres) + \
                 (brandy_price * brandy_litres) + (wine_price * wine_litres) + (beer_price * beer_litres)
print('%.2f' % final_expenses)

