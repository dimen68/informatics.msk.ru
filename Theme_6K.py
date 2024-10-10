# Удаление символа
str_ = input('Введите строку с цифрами: ')
count_ = str_.count('@')
for i in range(0, count_):
    to_del = str_.find('@')
    str_ = str_[0:to_del]+str_[to_del+1:]
print(str_)