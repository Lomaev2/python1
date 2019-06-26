H =int(input('Часов: '))
M =int(input('Минут: '))
S =int(input('Секунд: '))
H1 =int(input('Часов: '))
M1 =int(input('Минут: '))
S1 =int(input('Секунд: '))
minutes = H*60+M
seconds = minutes*60+S

minutes1 = H1*60+M1
seconds1 = minutes1*60+S1

print(seconds1-seconds)
