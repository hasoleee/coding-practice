A,B,C=map(int,input().split())
if B>=C:
    print("-1")
else:
    x=(A/(C-B))+1
    print(int(x))