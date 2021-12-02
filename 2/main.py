if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1
        pos = 0
        depth = 0
        for line in f.readlines():
            content = line.strip().split(' ')
            cmd = content[0]
            num = int(content[1])
            if cmd == 'forward':
                pos += num
            elif cmd == 'down':
                depth += num
            else:
                depth -= num
        print(pos, depth, pos * depth)

        # question 2
        pos = 0
        depth = 0
        aim = 0
        for line in f.readlines():
            content = line.strip().split(' ')
            cmd = content[0]
            num = int(content[1])
            if cmd == 'forward':
                pos += num
                depth += aim * num
            elif cmd == 'down':
                aim += num
            else:
                aim -= num
        print(pos, depth, pos * depth)
