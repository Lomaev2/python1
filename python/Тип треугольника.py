a=int(input())
b=int(input())
c=int(input())
if ((a%2==0 and b%2==1 and c%2==1) or (b%2==0 and a%2==1 and c%2==1)) or (c%2==0 and a%2==1 and b%2==1):
    print('YES')
else:
    print('no')
