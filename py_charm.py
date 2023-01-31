from random import randint
number = randint(1,1000)
count = 0
for run in range(6):
    your_number = int(input('Input your number: '))
    count +=1
    if your_number > number:
        print('No, the right is lower')
    elif your_number < number:
        print('No, the right is bigger')
    elif your_number == number:
        print(f'You win and used tries: {count}.')
        break

    if count == 6 and your_number !=number:
        print('You lost')