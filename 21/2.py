class Solution:
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second
        self.score1 = 0
        self.score2 = 0
        self.num1 = 0
        self.num2 = 0
        self.values = [3, 4, 5, 6, 7, 8, 9]
        self.times = [1, 3, 6, 7, 6, 3, 1]
        self.chance = 1
    
    def run(self, is_first):
        if self.score1 >= 21:
            self.num1 += self.chance
            return
        
        if self.score2 >= 21:
            self.num2 += self.chance
            return

        for i in range(len(self.values)):
            if is_first:
                old = self.first
                self.first = (self.first + self.values[i] - 1) % 10 + 1
                self.score1 += self.first
            else:
                old = self.second
                self.second = (self.second + self.values[i] - 1) % 10 + 1
                self.score2 += self.second
            self.chance *= self.times[i]

            self.run(not is_first)

            self.chance //= self.times[i]
            if is_first:
                self.score1 -= self.first
                self.first = old
            else:
                self.score2 -= self.second
                self.second = old


if __name__ == '__main__':
    s = Solution(5, 9)
    s.run(True)
    print(s.num1, s.num2)
