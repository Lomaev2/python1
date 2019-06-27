n=int(input())
z=n%10
print(z)
if n==1 or z==1:
    print('На лугу пасется',n,'корова')
elif n//10==1 or z//10==1:
    print('На лугу пасется',n,'коров')
elif (z==2 or z==3 or z==4) or (n==1 or n==3 or n==4):
    print('На лугу пасется',n,'коровы')
else:
    print('На лугу пасется',n,'коров')
