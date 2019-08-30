tables = int(input())
tablesLength = float(input())
tablesWidth = float(input())
coverArea = tables * (tablesLength + 2 * 0.30) * (tablesWidth + 2 * 0.30)
boxArea = tables * (tablesLength / 2) * (tablesLength / 2)
priceDollars = (coverArea * 7) + (boxArea * 9)
priceInBG = priceDollars * 1.85
print('%.2f' % priceDollars + ' USD')
print('%.2f' % priceInBG + ' BGN')