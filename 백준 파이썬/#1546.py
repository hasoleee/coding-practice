
sum=0
n=int(input())
grade=list(map(int,input().split()))
m=max(grade)
for i in range(len(grade)):
    grade[i]=grade[i]/m*100
    sum+=grade[i]
print(sum/len(grade))