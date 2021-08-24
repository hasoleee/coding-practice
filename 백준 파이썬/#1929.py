m,n=map(int,input().split())
for i in range(m,n+1):
    for j in range(2,n+1):
        count=0
        if i%j==0:
            count+=1
            if count<2:
                print(i)