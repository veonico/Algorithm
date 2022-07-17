# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import heapq

num_tc = 10

for tc_idx in range(num_tc):

    dump_count = int(input())

    boxes = list(map(int, input().split())) # min_heap
    boxes_negative = list(map(lambda x : x*-1, boxes)) # max_heap

    heapq.heapify(boxes)
    heapq.heapify(boxes_negative)

    while dump_count:

        hi = heapq.heappop(boxes_negative) * -1
        lo = heapq.heappop(boxes)

        if hi - lo <= 1:
            break

        heapq.heappush(boxes,lo+1)
        heapq.heappush(boxes_negative, -(hi-1))

        dump_count -= 1

    hi = heapq.heappop(boxes_negative) * -1
    lo = heapq.heappop(boxes)

    print(f"#{tc_idx+1} {hi-lo}")