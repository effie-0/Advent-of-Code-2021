def step(start, mapping):
    result = [start[0]]
    for i in range(len(start) - 1):
        pair = start[i:i + 2]
        result.append(mapping[pair])
        result.append(pair[1])
    return ''.join(result)

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
        
        result = start
        for i in range(10):
            result = step(result, mapping)
        
        counts = [result.count(x) for x in elements]
        print(counts, max(counts) - min(counts))
