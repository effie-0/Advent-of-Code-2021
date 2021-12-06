def day(fishes):
    count = 0
    num = len(fishes)
    for i in range(num):
        if fishes[i] == 0:
            count += 1
            fishes[i] = 6
        else:
            fishes[i] -= 1
    
    for i in range(count):
        fishes.append(8)


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        fishes = f.readline().split(',')
        fishes = [int(x) for x in fishes]

        for i in range(80):
            day(fishes)

        print(len(fishes))
