num_tc = int(input())

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

for tc_idx in range(num_tc):

    mat_len = int(input()) # size of matrix

    # initialize matrix

    matrix = [[-1]*(mat_len+2)]

    for _ in range(mat_len):
        temp = [-1] + [0]*mat_len + [-1]
        matrix.append(temp)

    matrix.append(matrix[0].copy())

    cur_row = 1
    cur_col = 1
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    dir_idx = 0
    num = 1

    while num <= mat_len**2:
        # numbering
        matrix[cur_row][cur_col] = num

        # check the next cell
        cur_dir = dirs[dir_idx]
        temp_row = cur_row + cur_dir[0]
        temp_col = cur_col + cur_dir[1]

        if matrix[temp_row][temp_col] != 0: # if unvalid
            dir_idx += 1
            if dir_idx == 4:
                dir_idx = 0
            cur_dir = dirs[dir_idx]

        cur_row += cur_dir[0]
        cur_col += cur_dir[1]

        num += 1

    print(f"#{tc_idx+1}")

    for row in matrix[1:-1]:
        temp = " ".join(list(map(str, row[1:-1])))
        print(temp)
