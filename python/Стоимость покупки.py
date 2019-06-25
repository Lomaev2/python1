A = int(input()) # Рубли    
B = int(input()) # Копейки
N = int(input()) # Кол-во
pricekop = (A * 100 + B) * N
print(pricekop//100, pricekop%100)
