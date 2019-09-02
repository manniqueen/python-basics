first = int(input())
second = int(input())
third = int(input())

result_seconds = first + second + third
minutes = result_seconds // 60
seconds = result_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")