class Solution:
    def __init__(self, enhance_map, image) -> None:
        self.enhance_map = enhance_map
        self.image = image
        self.m = len(image)
        self.n = len(image[0])
        self.times = 0
    
    def get(self, i, j):
        if 0 <= i and i < self.m and 0 <= j and j < self.n:
            return self.image[i][j]
        else:
            if self.times % 2:
                return '.'
            else:
                return '#'
    
    def enhance(self):
        new_image = []
        self.times += 1

        for i in range(-1, self.m + 1):
            new_line = []
            for j in range(-1, self.n + 1):
                code = ''
                
                for _i in range(-1, 2):
                    for _j in range(-1, 2):
                        code += self.get(i + _i, j + _j)
                
                value = []
                for ch in code:
                    if ch == '.':
                        value.append('0')
                    else:
                        value.append('1')
                
                value = ''.join(value)
                value = int(value, 2)
                new_line.append(self.enhance_map[value])

            new_image.append(new_line)
        
        self.image = new_image
        self.m = len(self.image)
        self.n = len(self.image[0])
    
    def count(self):
        num = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.image[i][j] == '#':
                    num += 1
        
        return num

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        enhance_map = None
        image = []
        
        for line in f.readlines():
            content = line.strip()
            if not len(content):
                continue

            if not enhance_map:
                enhance_map = content
            else:
                image.append(content)

        s = Solution(enhance_map, image)

        for i in range(50):
            s.enhance()
        print(s.count())
