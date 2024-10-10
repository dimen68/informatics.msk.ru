# Второе вхождение
stroka = input('введите строку: ')
result_ = 0
if stroka.find('f') != -1:
    first_ = stroka.find('f')
    result_ = -1
    if stroka.find('f', first_) != -1:
        result_ = stroka.find('f', first_+1)
else:
    result_ = -2
print(result_)