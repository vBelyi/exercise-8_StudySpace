from random import randint
number = randint(1,100)
n = 6
count = 0
for run in range(n):
    your_number = int(input('Давай зіграєм у гру. Введи своє число: '))
    count +=1
    if your_number > number:
        print('Ніііі, правильне число меньше')
    elif your_number < number:
        print('Ніііі, правильне число більше')
    elif your_number == number:
        print(f'Перемога, ти відгадав число!!!Кількість спроб: {count}.')
        break

    if count == n and your_number !=number:
        print('Твої спроби закінчились, ти програв!')