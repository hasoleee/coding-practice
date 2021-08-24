word=list(input())
word_list=list(map(chr,range(65,91)))
sum=0
for i in word:
    if i in word_list[0:3]:
        sum+=3
    elif i in word_list[3:6]:
        sum+=4
    elif i in word_list[6:9]:
        sum+=5
    elif i in word_list[9:12]:
        sum+=6
    elif i in word_list[12:15]:
        sum+=7
    elif i in word_list[15:19]:
        sum+=8
    elif i in word_list[19:22]:
        sum+=9
    else:
        sum+=10

print(sum)
    

