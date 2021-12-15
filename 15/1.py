from queue import PriorityQueue


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        risk_map = []
        for line in f.readlines():
            content = [int(x) for x in line.strip()]
            risk_map.append(content)
        
        m = len(risk_map)
        n = len(risk_map[0])

        q = PriorityQueue()
        q.put((0, 0, 0))
        values = {}

        while not q.empty():
            value, x, y = q.get()
            if x == m - 1 and y == n - 1:
                print(value)
                break

            for _x, _y in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if _x < 0 or _x >= m or _y < 0 or _y >= n:
                    continue
                
                new_value = value + risk_map[_x][_y]
                if (_x, _y) in values and values[(_x, _y)] <= new_value:
                    continue
                
                values[(_x, _y)] = new_value
                q.put((new_value, _x, _y))
