text = input()
a = 1
e = 2
i_i = 3
o = 4
u = 5
sum = 0

for i in text:
    if i == 'a':
        sum += a
    elif i == 'e':
        sum += e
    elif i == 'i':
        sum += i_i
    elif i == 'o':
        sum += o
    elif i == 'u':
        sum += u

print(sum)