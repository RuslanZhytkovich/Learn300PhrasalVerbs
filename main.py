import random

mydict = {
    'hello': 'привет',
    'home': 'дом',
    'cat': 'кот',
    'dog': 'собака',
    'table': 'стол',
    'laptop':'ноутбук'
}



temp_list = []


lst = list(mydict.items())
pair = lst[random.randint(0,len(mydict) - 1)]

eng_word = pair[0]
rus_word = pair[1]

temp_list.append(eng_word)

counter = 0
while(counter != 3):
    pair = lst[random.randint(0,len(mydict) - 1)]
    temp_word = pair[0]
    if(temp_word not in temp_list):
        temp_list.append(temp_word)
        counter += 1



random.shuffle(temp_list)

print(eng_word, '-', rus_word)

print(f'Введите правильное значение слова {rus_word}: ')
print(f'1){temp_list[0]}\n2){temp_list[1]}\n3){temp_list[2]}\n4){temp_list[3]}')
a = input("Ваш ответ: ")
if(a==eng_word):
    print("Верно")
else:
    print("Неверно, правильный ответ: ", eng_word )











