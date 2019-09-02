start_hours = int(input())
start_minutes = int(input())

time_in_minutes = start_hours * 60 + start_minutes

time_plus_15 = time_in_minutes + 15

final_hours = time_plus_15 // 60
final_minutes = time_plus_15 % 60

if final_hours > 23:
    final_hours = final_hours - 24

if final_minutes < 10:
    print(f"{final_hours}:0{final_minutes}")
else:
    print(f"{final_hours}:{final_minutes}")