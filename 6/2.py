if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        fishes = f.readline().split(',')
        fishes = [int(x) for x in fishes]

        counts = [fishes.count(i) for i in range(9)]
        for i in range(256):
            new_fishes = counts.pop(0)
            counts[6] += new_fishes
            counts.append(new_fishes)
        
        print(sum(counts))
