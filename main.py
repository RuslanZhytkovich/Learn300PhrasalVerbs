import random
from files import read_file


mydict = read_file('words.txt')


def clear():
    print('\n'*20)

correct_answers = 0
incorrect_answers = 0

list_of_used_word =[]                  # список для использованных слов
lst = list(mydict.items())             # cписок из ключей и значений словаря
exit = False

name = input('Добро пожаловать! Введите свое имя: ')
clear()
iterations = 0     # чтобы знать сколько раз срабатывал цикл

while((len(list_of_used_word) != len(mydict)) and exit == False):
    temp_list = []                    # список для вариантов ответа

    pair = lst[random.randint(0, len(mydict) - 1)]      # извлекаем из списка пару

    eng_word = pair[0]
    rus_word = pair[1]

    temp_list.append(eng_word)                     # в варианты ответа добавляем правильный ответ

    if(eng_word not in list_of_used_word):       # проверка на то, использовали ли мы уже это слово
        list_of_used_word.append(eng_word)                  # если не использовали то добавляем в список использованных

        while(len(temp_list) != 4):
            answer = lst[random.randint(0, len(mydict) - 1)][0]

            if((answer != eng_word) and (answer not in temp_list)):
                temp_list.append(answer)


        random.shuffle(temp_list)

        iterations += 1


        print(f'Введите правильное значение слова {rus_word}: ')
        print(f'1){temp_list[0]}\n2){temp_list[1]}\n3){temp_list[2]}\n4){temp_list[3]}\n5)exit - для завершения программы')

        a = ""
        while(a not in temp_list):
            a = input("Ваш ответ: ")

            if (a == 'exit'):
                exit = True
                break
            elif (a == eng_word):
                clear()
                print("Верно\n\n")
                correct_answers += 1

            elif (a in temp_list and a != eng_word):
                print("Неверно, правильный ответ: ", eng_word, '\n\n')
                incorrect_answers += 1






clear()
if (correct_answers == 0 and iterations > 5):
    print(f'{name}! Вы ни ответили правильно не на один вопрос! Пора браться за ум.')

else:
    print(f'{name}! Ваш результат {correct_answers} из {iterations-1}.')


file_write = open('results.txt','a',encoding='utf-8')
file_write.write(f'\nРезультат пользователя "{name}" {correct_answers} из {iterations-1}')













