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
            if x == 5 * m - 1 and y == 5 * n - 1:
                print(value)
                break

            for _x, _y in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                if _x < 0 or _x >= 5 * m or _y < 0 or _y >= 5 * n:
                    continue
                
                div_x = _x // m
                mod_x = _x % m
                div_y = _y // n
                mod_y = _y % n

                risk = (risk_map[mod_x][mod_y] + div_x + div_y - 1) % 9 + 1
                new_value = value + risk
                if (_x, _y) in values and values[(_x, _y)] <= new_value:
                    continue
                
                values[(_x, _y)] = new_value
                q.put((new_value, _x, _y))
