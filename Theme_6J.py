# Замена подстроки
str_ = input('Введите строку с цифрами: ')
count_ = str_.count('1')
for i in range(0, count_):
    arg_now = str_.find('1')
    str_ = str_[0:arg_now]+'one' + str_[arg_now+1:]
print(str_)