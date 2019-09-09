max_poor_grades = int(input())
task = input()

poor_grades = 0
sum_grades = 0
count_tasks = 0
last_task = None

while task != 'Enough':
    grade = int(input())
    sum_grades += grade
    count_tasks += 1

    if grade <= 4:
        poor_grades += 1

    if poor_grades == max_poor_grades:
        print(f'You need a break, {poor_grades} poor grades.')
        break

    last_task = task
    task = input()
    
    
if task == 'Enough':

    average = sum_grades * 1.0 / count_tasks
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {count_tasks}')
    print(f'Last problem: {last_task}')










