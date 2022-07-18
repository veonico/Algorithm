# 1209. [S/W 문제해결 기본] 2일차 - Sum
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

num_tc = 10

for _ in range(num_tc):

    tc_idx = int(input())

    garo_sum = []
    sero_sum = [0]*100
    dagag_sum = [0]*2

    for row_idx in range(100):

        row = list(map(int, input().split()))
        garo_sum.append(sum(row))

        for col_idx in range(100):
            sero_sum[col_idx] += row[col_idx]
            if row_idx == col_idx:
                dagag_sum[0] += row[col_idx]
            elif row_idx + col_idx == 99:
                dagag_sum[1] += row[col_idx]

    answer = max(max(garo_sum), max(sero_sum), max(dagag_sum))
    print(f"#{tc_idx} {answer}")






