class Solution:
    def __init__(self):
        self.versions = 0
    
    def parse(self, value, is_subpacket):
        if len(value) < 6:
            return len(value)
        
        version = int(value[:3], 2)
        self.versions += version
        type = int(value[3:6], 2)
        
        if type == 4:
            # literal value
            i = 6
            while True:
                if value[i] == '0':
                    i += 5
                    break
                i += 5
            if not is_subpacket:
                i = (i + 4) // 4 * 4
            return i
        else:
            if len(value) < 7:
                return len(value)
            length_type = int(value[6])
            if length_type == 0:
                length = int(value[7:22], 2)
                start = 22
                while length > 0:
                    sublen = self.parse(value[start:start + length], True)
                    start += sublen
                    length -= sublen
                return start
            else:
                num = int(value[7:18], 2)
                start = 18
                for i in range(num):
                    sublen = self.parse(value[start:], True)
                    start += sublen
                return start

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        line = f.readline().strip()
        binary = bin(int(line, 16))[2:].zfill(4 * len(line))
        s = Solution()
        s.parse(binary, False)
        print(s.versions)
