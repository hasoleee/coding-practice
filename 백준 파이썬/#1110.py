n=int(input())
new=n
circle=0
while (True):
    a=new/10
    b=new%10
    c=(a+b)%10
    new=10*b+c
    circle=+1
    if (n==new):
        break
    print(circle)
