# Первое и последнее вхождение F
stroka = input('Введите слово: ')
first_in =  stroka.find('f')
if first_in != -1:
    print(first_in)
last_in =  stroka.rfind('f',first_in+1)
if last_in != -1:
    print(last_in)
