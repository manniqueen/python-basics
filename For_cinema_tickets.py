total_tickets = 0
student = 0
standard = 0
kid = 0
percentage_students = 0
percentage_standard = 0
percentage_kid = 0
movie_tickets = input()

while movie_tickets == 'Finish':

    free_seats = int(input())

    for ticket in range(0, free_seats + 1):
        ticket_type = input()
        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1
        elif ticket_type == "End":
            break
        elif ticket_type == "Finish":
            break

    percentage_busy = (ticket / free_seats) * 100
    print(f"{movie_name} - {percentage_busy:.2f}% full.")
    if ticket_type == "Finish":
        total_tickets = standard + student + kid
        percentage_students = (student / total_tickets) * 100
        percentage_standard = (standard / total_tickets) * 100
        percentage_kid = (kid / total_tickets) * 100
        print(f"Total tickets: {total_tickets}")
        print(f"{percentage_students:.2f}% student tickets.")
        print(f"{percentage_standard:.2f}% standard tickets.")
        print(f"{percentage_kid:.2f}% kids tickets.")