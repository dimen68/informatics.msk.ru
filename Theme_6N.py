# Удалить каждый третий символ
str_ = input('Введите строку: ')
print(id(str_))
str_new = ''
for i in range(0, len(str_)):
    if i % 3 != 0:
        str_new += str_[i]
str_ = str_new
print(id(str_))
print(str_)
