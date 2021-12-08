if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        counts = 0
        for line in f.readlines():
            content = line.strip().split(' | ')
            outs = content[1].split()
            for out in outs:
                if len(out) == 2 or len(out) == 4 or len(out) == 3 or len(out) == 7:
                    counts += 1
        print(counts)
