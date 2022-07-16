# 2085. 농작물 수확하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

num_tc = int(input())

for tc_idx in range(num_tc):
    mat_len = int(input()) # size of matrix

    start = (mat_len//2)+1
    end = (mat_len//2)

    answer = 0
    border = mat_len//2

    for row_idx in range(mat_len):

        in_str = list(input())
        row = list(map(int, in_str))

        if row_idx <= border:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

        answer += sum(row[start:end])

    print(f"#{tc_idx+1} {answer}")
            
            


