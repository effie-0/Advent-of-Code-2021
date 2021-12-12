class Solution:
    def __init__(self, inputs):
        self.pairs = inputs
        self.mapping = {}
        self.num = 0
        self.small = False
        for pair in self.pairs:
            if not pair[0] in self.mapping:
                self.mapping[pair[0]] = [pair[1]]
            else:
                self.mapping[pair[0]].append(pair[1])
            
            if not pair[1] in self.mapping:
                self.mapping[pair[1]] = [pair[0]]
            else:
                self.mapping[pair[1]].append(pair[0])

    def run(self):
        visited = {'start': 1}
        self.step(visited, 'start')
        return self.num
    
    def step(self, visited, current):
        if current == 'end':
            self.num += 1
            return
        
        for point in self.mapping[current]:
            changed = False
            if point.islower() and point in visited and visited[point] > 0:
                if not self.small and point not in ['start', 'end'] and visited[point] == 1:
                    changed = True
                    self.small = True
                else:
                    continue

            if not point in visited:
                visited[point] = 1
            else:
                visited[point] += 1
            
            self.step(visited, point)

            visited[point] -= 1
            if changed:
                self.small = False


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        pairs = []
        for line in f.readlines():
            content = line.strip().split('-')
            pairs.append((content[0], content[1]))
        
        s = Solution(pairs)
        num = s.run()
        print(num)
