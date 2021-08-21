code=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
for i in code:
    word=word.replace(i,'*')
print(len(word))