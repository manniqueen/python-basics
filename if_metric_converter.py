value = float(input())
edinica_in = input()
edinica_out = input()

if edinica_in == 'mm':
    value = value / 1000
elif edinica_in == 'cm':
    value = value / 100
if edinica_out == 'mm':
    value = value * 1000
elif edinica_out == 'cm':
    value = value * 100

print(f"{value:.3f}")