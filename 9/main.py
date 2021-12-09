def which_basin(mapping, low_map, basin_sizes, i, j, low_num, m, n):
    if low_map[i][j] != 0:
        return
    
    if mapping[i][j] == 9:
        return
    
    low_map[i][j] = low_num + 1
    basin_sizes[low_num] += 1

    if i != 0:
        which_basin(mapping, low_map, basin_sizes, i - 1, j, low_num, m, n)
    
    if i != m - 1:
        which_basin(mapping, low_map, basin_sizes, i + 1, j, low_num, m, n)

    if j != 0:
        which_basin(mapping, low_map, basin_sizes, i, j - 1, low_num, m, n)
    
    if j != n - 1:
        which_basin(mapping, low_map, basin_sizes, i, j + 1, low_num, m, n)


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1
        mapping = []
        for line in f.readlines():
            content = line.strip()
            points = [ord(x) - ord('0') for x in content]
            mapping.append(points)
        
        lows = []
        m = len(mapping)
        n = len(mapping[0])
        low_pos = []

        for i in range(m):
            for j in range(n):
                check = True

                if i != 0 and mapping[i][j] >= mapping[i - 1][j]:
                    check = False
                
                if i != m - 1 and mapping[i][j] >= mapping[i + 1][j]:
                    check = False
                
                if j != 0 and mapping[i][j] >= mapping[i][j - 1]:
                    check = False
                
                if j != n - 1 and mapping[i][j] >= mapping[i][j + 1]:
                    check = False
                
                if check:
                    lows.append(mapping[i][j])
                    low_pos.append((i, j))
        print(sum(lows), len(lows), sum(lows) + len(lows))
        
        # question 2
        basin_sizes = [0] * len(lows)
        low_map = [[0] * n for _ in range(m)]
        idx = 0
        for pos in low_pos:
            i, j = pos
            which_basin(mapping, low_map, basin_sizes, i, j, idx, m, n)
            idx += 1
        
        sizes = sorted(basin_sizes, reverse=True)
        print(sizes[0] * sizes[1] * sizes[2])
