seconds = float(input())
distance = float(input())
one_meter = float(input())

nujnisec = distance * one_meter
dobavka = (distance // 15) * 12.5
obshto = nujnisec + dobavka


if obshto < seconds:
    print(f"Yes, he succeeded! The new world record is {obshto:.2f} seconds.")
else:
    print(f"No, he failed! He was {obshto-seconds:.2f} seconds slower.")