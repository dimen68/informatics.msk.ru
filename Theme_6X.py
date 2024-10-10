# Вставка символов
str_ = input('Введите строку: ')
str_new = ''
for i in str_:
    str_new += i+'*'
str_new = str_new[0:-1]
print(str_new)