# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


from collections import deque

num_tc = 10

def is_palindrome(arr):

    result = True

    lo = 0
    hi = len(arr)-1

    while lo < hi:

        if arr[lo] != arr[hi]:
            result = False
            break
        
        lo += 1
        hi -= 1

    return result

def are_palindrome(arr, pal_len):

    init = deque(arr[:pal_len-1])
    result = 0

    for idx in range(pal_len-1, len(arr)):
        init.append(arr[idx])

        is_pal = is_palindrome(init)
        if is_pal:
            #print(init)
            result += 1

        init.popleft()

    return result

for idx_tc in range(num_tc):

    answer = 0
    len_obj = int(input())

    # get input
    matrix = [input() for _ in range(8)]

    # get number of palindromes
    for row in matrix:
        answer += are_palindrome(row, len_obj)
    
    # transpose
    matrix = list(zip(*matrix))

    for row in matrix:
        answer += are_palindrome(row, len_obj)

    print(f"#{idx_tc+1} {answer}")

    
