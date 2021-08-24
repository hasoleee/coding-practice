
def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)
n=int(input())
print(factorial(n))


n=int(input())
result=1
for i in range(1,n+1):
    result=result*i
print(result) 
