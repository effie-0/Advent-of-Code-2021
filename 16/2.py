import math

class Solution:
    def __init__(self):
        self.versions = 0
        self.value = 0
    
    def parse(self, value, is_subpacket):
        if len(value) < 6:
            return len(value)
        
        version = int(value[:3], 2)
        self.versions += version
        type = int(value[3:6], 2)
        
        if type == 4:
            # literal value
            i = 6
            val_str = ""
            while True:
                val_str += value[i + 1:i + 5]
                if value[i] == '0':
                    i += 5
                    break
                i += 5
            if not is_subpacket:
                i = (i + 4) // 4 * 4
            
            self.value = int(val_str, 2)
            return i
        else:
            if len(value) < 7:
                return len(value)
            length_type = int(value[6])
            sub_values = []
            
            start = 0
            if length_type == 0:
                length = int(value[7:22], 2)
                start = 22
                while length > 0:
                    sublen = self.parse(value[start:start + length], True)
                    sub_values.append(self.value)
                    start += sublen
                    length -= sublen
            else:
                num = int(value[7:18], 2)
                start = 18
                for i in range(num):
                    sublen = self.parse(value[start:], True)
                    sub_values.append(self.value)
                    start += sublen
            
            if type == 0:
                self.value = sum(sub_values)
            elif type == 1:
                self.value = math.prod(sub_values)
            elif type == 2:
                self.value = min(sub_values)
            elif type == 3:
                self.value = max(sub_values)
            elif type == 5:
                if sub_values[0] > sub_values[1]:
                    self.value = 1
                else:
                    self.value = 0
            elif type == 6:
                if sub_values[0] < sub_values[1]:
                    self.value = 1
                else:
                    self.value = 0
            else:
                if sub_values[0] == sub_values[1]:
                    self.value = 1
                else:
                    self.value = 0
            
            return start

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        line = f.readline().strip()
        binary = bin(int(line, 16))[2:].zfill(4 * len(line))
        s = Solution()
        s.parse(binary, False)
        print(s.versions)
        print(s.value)
