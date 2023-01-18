# 39(1). Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил
import random

sweets = 221
max_step = 28

step = random.choice(['Player1','Player2'])
while sweets>0:
    print('Ход',step)
    get = int(input('Ваш ход -'))
    while get<0 or get>max_step or get>sweets:
        print(f'{step} ваш ход не верный')
        get = int(input('Сделайте правильный ход -'))
    sweets = sweets - get
    if sweets >0:
        print(f'Осталось {sweets} конфет')
    else:
        print(f'Конфет не осталось')
    if sweets<=0:
        print(f"Выиграл игрок {step}")

    if step =="Player1":
        step ="Player2"
    else: step ="Player1"

