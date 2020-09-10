print("""
Please pick a number between 1 and 100 and I will guess that number
sounds cool, lets get started:-
you only will enter one of the following keys:-
 u if my guess is higher then your number
 d if my guess is lower then your number
 c if my guess is correct
 q to quit
""")


numbers = range(1, 101)
while True:
    guess = numbers[len(numbers)//2]
    print(f'My guess is {guess} is this correct')
    key = input('Please enter an option: ')
    index = numbers.index(guess)
    if key == 'd':
        numbers = numbers[index:]
    elif key == 'u':
        numbers = numbers[:index]
    elif key == 'c':
        print('Cool I knew it')
        break
    elif key == 'q':
        print('Ok I understand you are busy now! hope to see you soon')
        break
    else:
        print('Please select one of the above options')