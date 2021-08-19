iter_count = int(input())

for count in range(iter_count):
    result_list = list(input())
    
    score = 0
    total_score = 0
    for result in result_list:
        if result == "o":
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)