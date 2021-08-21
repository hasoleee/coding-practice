
n=int(input())
for _ in range(n):
    sum=0
    total=0
    grade=list(input())
    for i in grade:
        if i=='O':
                sum+=1
                total=total+sum
        else:
            sum=0
    print(total)