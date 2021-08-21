n=int(input())
result=0
for i in range(n):
    word=input()
    if list(word)==sorted(word,key=word.find):
        result+=1
print(result)