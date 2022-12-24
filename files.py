
def read_file(filename):

    eng_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    file = open('words.txt', encoding='utf-8')
    lst = []
    for row in file:
        lst.append(row.replace('\n', ''))

    word_dict = {}

    for i in lst:
        temp_lst = i.split(' - ')
        temp_lst[0]= temp_lst[0].replace('4','').replace('2','').replace('1','').replace('3','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9', '').replace('0','').replace('.','').strip()
        word_dict[temp_lst[0]] = temp_lst[1]

    return word_dict






