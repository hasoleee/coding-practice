hour, min = map(int, input().split())

if min - 45 < 0:
    new_min = 60 - (45 - min)
    if hour == 0:
        new_hour = 23
    else:
        new_hour = hour - 1
else:
    new_min = min - 45
    new_hour = hour
print(str(new_hour)+' '+str(new_min))