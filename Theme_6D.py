# Переставьте эти слова местами
fraza = input('Введите фразу из двух слов: ')
index_ = fraza.find(' ')
fraza_new = fraza[(index_+1)::] + ' ' + fraza[0:(index_+1)]
print(fraza_new)