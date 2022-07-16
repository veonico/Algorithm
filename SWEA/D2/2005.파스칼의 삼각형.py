# 2005.파스칼의 삼각형
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

num_tc = int(input())
tcs = []
for _ in range(num_tc):
    tri_size = int(input())
    tcs.append(tri_size)

for tc_idx, tri_size in enumerate(tcs):
    answers = [[1]]

    if tri_size >= 2:
        answers.append([1,1])

    if tri_size >= 3: # if triangle side is bigger than 2

        while tri_size >= 3:

            temp = [1]
            top = answers[-1]

            for idx in range(len(top)-1):
                temp.append(top[idx] + top[idx+1])

            temp.append(1)
            answers.append(temp)
            tri_size -= 1

    print(f"#{tc_idx+1}")
    for row in answers:
        print(" ".join(list(map(str, row))))


