# 2007. 패턴 마디의 길이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


num_tc = int(input())

for tc_idx in range(num_tc):
    txt = list(input())
    answer = 0

    for madi_len in range(1, len(txt)//2):
        madi = txt[:madi_len]

        # get the maximum multiple less than 30
        indices = []

        for i in range(30):
            temp = (i+1)*madi_len
            if temp < 30:
                indices.append(i*madi_len)

        #print(indices)

        continue_flag = 0
        # compare
        for idx in indices:
            compare_madi = txt[idx:idx+madi_len]
            if compare_madi != madi:
                continue_flag = 1
                break

        if continue_flag:
            continue

        else:
            answer = madi_len
            break
    
    print(f"#{tc_idx+1} {answer}")