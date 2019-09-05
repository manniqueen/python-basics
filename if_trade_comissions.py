city = input()
price = float(input())
result = 0

if city == 'Sofia':
    if 0 <= price <= 500:
        result = price * (5 / 100)
    elif price > 500 and price <= 1000:
        result = price * (7 / 100)
    elif price > 1000 and price <= 10000:
        result = price * (8 / 100)
    elif price > 10000:
        result = price * (12 / 100)
    else:
        print("error")
elif city == 'Varna':
    if 0 <= price <= 500:
        result = price * (4.5 / 100)
    elif price > 500 and price <= 1000:
        result = price * (7.5 / 100)
    elif price > 1000 and price <= 10000:
        result = price * (10 / 100)
    elif price > 10000:
        result = price * (13 / 100)
    else:
        print("error")
elif city == 'Plovdiv':
    if 0 <= price <= 500:
        result = price * (5.5 / 100)
    elif price > 500 and price <= 1000:
        result = price * (8 / 100)
    elif price > 1000 and price <= 10000:
        result = price * (12 / 100)
    elif price > 10000:
        result = price * (14.5 / 100)
    else:
        print("error")
else:
    print("error")
    
if not result == 0:
    print(f"{result:.2f}")