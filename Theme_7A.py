# Список квадратов
N = int(input('Введите число: '))
list_ =[]
for i in range(1, N):
    n = i ** 2
    if n < N:
        list_.append(n)
    else:
        break
print(list_)
