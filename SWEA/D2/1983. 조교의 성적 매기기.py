# 1983. 조교의 성적 매기기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

num_tc = int(input())

def calculate_score(string):
    # arr : [중간고사, 기말고사, 과제]
    arr = list(map(int, string.split()))
    return arr[0]*.35 + arr[1]*.45 + arr[2]*.2

score_list = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]

for tc_idx in range(num_tc):
    num_st, no_st = map(int, input().split())
    no_st -= 1
    scores = []

    for st_idx in range(num_st):
        scores.append((st_idx, calculate_score(input())))

    scores = sorted(scores, key = lambda k : k[1], reverse = True)
    
    for st_id, score_info in enumerate(scores):
        #print(st_id, score_info)
        if no_st == score_info[0]:
            answer = int((st_id)*10/num_st)
            #print(answer)
            break

    print(f"#{tc_idx+1} {score_list[answer]}")
