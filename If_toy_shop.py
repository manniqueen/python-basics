trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
lorries_count = int(input())

all_things_sum = (puzzle_count * 2.60) + (dolls_count * 3.0) \
                 + (bears_count * 4.10) + (minions_count * 8.20) + (lorries_count * 2.0)

all_things_count = puzzle_count + dolls_count + bears_count + minions_count + lorries_count

if all_things_count >= 50:
    all_things_sum = all_things_sum - (all_things_sum * 0.25)
all_things_sum = all_things_sum - (all_things_sum * 0.1)

if all_things_sum >= trip_price:
    result = all_things_sum - trip_price
    print('Yes! %.2f lv left.' % result)
else:
    print('Not enough money! %.2f lv needed.' % (trip_price - all_things_sum))


