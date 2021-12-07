if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        pos = f.readline().strip().split(',')
        pos = [int(x) for x in pos]
        min_ = min(pos)
        max_ = max(pos)

        counts = [0] * (max_ - min_ + 1)
        for i in range(min_, max_ + 1):
            counts[i - min_] = pos.count(i)
        
        fuels = [0] * (max_ - min_ + 1)
        for i in range(min_, max_ + 1):
            for j in range(min_, max_ + 1):
                x = abs(j - i)
                fuels[i - min_] += counts[j - min_] * (1 + x) * x / 2
        
        print(min(fuels))
