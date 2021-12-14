def step(pair_counts, mapping):
    result = {}
    for pair in mapping.keys():
        result[pair] = 0

    for pair, count in pair_counts.items():
        mid = mapping[pair]
        left = pair[0] + mid
        right = mid + pair[1]

        result[left] += count
        result[right] += count
    
    return result

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        start = ''
        mapping = {}
        elements = []
        
        for line in f.readlines():
            content = line.strip()
            if len(start) == 0:
                start = content
                continue

            if len(content) == 0:
                continue

            content = content.split(' -> ')
            mapping[content[0]] = content[1]
            if content[0][0] not in elements:
                elements.append(content[0][0])
            
            if content[0][1] not in elements:
                elements.append(content[0][1])
        
        pair_counts = {}
        for i in range(len(start) - 1):
            pair = start[i:i + 2]
            if pair not in pair_counts:
                pair_counts[pair] = 1
            else:
                pair_counts[pair] += 1

        for i in range(40):
            pair_counts = step(pair_counts, mapping)
        
        counts = {}
        for pair, count in pair_counts.items():
            if pair[0] not in counts:
                counts[pair[0]] = count
            else:
                counts[pair[0]] += count
            
            if pair[1] not in counts:
                counts[pair[1]] = count
            else:
                counts[pair[1]] += count
        
        counts[start[0]] += 1
        counts[start[-1]] += 1
        
        print((max(counts.values()) - min(counts.values())) / 2)
