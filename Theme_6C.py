# Разрежьте ее на две равные части

str_ = input('Введите слово: ')
l_half = len(str_)//2
nechet = (len(str_)) % 2
str_new = str_[(l_half+nechet)::] + str_[0:(l_half+nechet)]
print(str_new)