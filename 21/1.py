class Solution:
    def __init__(self, first, second) -> None:
        self.first = first
        self.second = second
        self.score1 = 0
        self.score2 = 0
        self.current = 1
    
    def run(self):
        is_first = True
        while self.score1 < 1000 and self.score2 < 1000:
            if is_first:
                self.first = (self.first + 3 * self.current + 2) % 10 + 1
                self.score1 += self.first
                is_first = False
            else:
                self.second = (self.second + 3 * self.current + 2) % 10 + 1
                self.score2 += self.second
                is_first = True
            self.current += 3


if __name__ == '__main__':
    s = Solution(5, 9)
    s.run()
    print(s.score1, s.score2, s.current - 1, (s.current - 1) * min(s.score1, s.score2))
