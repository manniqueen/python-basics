searched_book = input()
capacity = int(input())
counter = 0
is_found = False

while counter < capacity:
    current_book = input()
    if current_book == searched_book:
        is_found = True
        break

    counter += 1
    if counter == capacity:
        break



if is_found:
    print(f'You checked {counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')
