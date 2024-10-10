# Удаление фрагмента
stroka = input('Введите строку с буквами h: ')
if stroka.find('h') != -1:
    first_ = stroka.find('h')
    if stroka.find('h', first_ + 1) != -1:
        last_ = stroka.rfind('h')
    else:
        print('В этой строке только одна буква h')
else:
    print('В той строке нет буквы h')
print(stroka[0:first_] + stroka[last_+1:])
