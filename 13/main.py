class Solution:
    def __init__(self, points, folds):
        self.points = points
        self.folds = folds

        max_val = max([max(point) for point in points]) + 1
        self.mapping = [[0] * max_val for _ in range(max_val)]
        for point in points:
            self.mapping[point[1]][point[0]] = 1
    
    def fold(self, is_x, value):
        new_map = []
        m = len(self.mapping)
        n = len(self.mapping[0])
        
        if is_x:
            for y in range(m):
                new_map.append(self.mapping[y][:value])
                for x in range(value + 1, n):
                    if self.mapping[y][x]:
                        pos = value - (x - value)
                        if pos >= 0 and not self.mapping[y][pos]:
                            new_map[y][pos] = 1
        else:
            for y in range(value):
                new_map.append(self.mapping[y])
            
            for y in range(value + 1, m):
                pos = value - (y - value)
                if pos < 0:
                    break
                
                for x in range(n):
                    if self.mapping[y][x] and not self.mapping[pos][x]:
                        new_map[pos][x] = 1
        
        self.mapping = new_map
    
    def fold_once(self, i):
        content = self.folds[i].split('=')
        is_x = False
        if content[0] == 'x':
            is_x = True
        value = int(content[1])
        
        # self.print()
        self.fold(is_x, value)
        num = sum([sum(line) for line in self.mapping])
        # self.print()
        return num

    def print(self):
        print('')
        for line in self.mapping:
            string = ''
            for val in line:
                if val:
                    string += '#'
                else:
                    string += '.'
            print(string)
    
    def complete(self):
        for i in range(len(self.folds)):
            self.fold_once(i)
        self.print()

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        points = []
        folds = []
        is_fold = False
        
        for line in f.readlines():
            content = line.strip()
            if len(content) == 0:
                is_fold = True
                continue
            
            if is_fold:
                folds.append(content[11:])
            else:
                content = [int(x) for x in content.split(',')]
                points.append(content)
        
        s = Solution(points, folds)
        num = s.fold_once(0)
        print(num)

        s.complete()
