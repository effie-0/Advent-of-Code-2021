if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        vents = []
        max_x = 0
        max_y = 0
        for line in f.readlines():
            content = line.strip().split(' -> ')
            point1 = content[0].split(',')
            point2 = content[1].split(',')
            point1 = [int(x) for x in point1]
            point2 = [int(x) for x in point2]
            vents.append([point1, point2])

            if point1[0] > max_x:
                max_x = point1[0]
            if point1[1] > max_y:
                max_y = point1[1]
            
            if point2[0] > max_x:
                max_x = point2[0]
            if point2[1] > max_y:
                max_y = point2[1]

        diagram = [[0] * (max_y + 1) for _ in range(max_x + 1)]

        for vent in vents:
            point1 = vent[0]
            point2 = vent[1]

            if point1[0] != point2[0] and point1[1] != point2[1]:
                x_inc, y_inc = 1, 1
                if point1[0] > point2[0]:
                    x_inc = -1
                if point1[1] > point2[1]:
                    y_inc = -1
                
                j = point1[1]
                for i in range(point1[0], point2[0] + x_inc, x_inc):
                    diagram[i][j] += 1
                    j += y_inc

            elif point1[0] == point2[0]:
                if point1[1] <= point2[1]:
                    for i in range(point1[1], point2[1] + 1):
                        diagram[point1[0]][i] += 1
                else:
                    for i in range(point2[1], point1[1] + 1):
                        diagram[point1[0]][i] += 1

            elif point1[1] == point2[1]:
                if point1[0] <= point2[0]:
                    for i in range(point1[0], point2[0] + 1):
                        diagram[i][point1[1]] += 1
                else:
                    for i in range(point2[0], point1[0] + 1):
                        diagram[i][point1[1]] += 1
        
        count = 0
        for line in diagram:
            for point in line:
                if point >= 2:
                    count += 1
        
        print(count)
