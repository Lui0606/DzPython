import random

word = random.choice(['колобок'])

word_list = ['_' for i in word]
# print(word_list)

lives = 3

while True:
    user_letter = input('Введи букву: ')
    find_letter = False
    for index, letter in enumerate(word):
        if user_letter == letter:
            find_letter = True
            word_list[index] = letter

    if not find_letter:
        lives -= 1
        print('Не угадал!')
        if lives == 0:
            print('Ты проиграл!')
            break
        print(f'Осталось попыток: {lives}')

    user_word = ("".join(word_list))
    print(user_word)

    if user_word == word:
        print('Отгадал!')
        break