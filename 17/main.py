class Solution:
    def __init__(self, v_x, v_y) -> None:
        self.area_left, self.area_right = 57, 116
        self.area_up, self.area_bottom = -148, -198
        self.v_x = v_x
        self.v_y = v_y
        self.x = 0
        self.y = 0

    def work(self):
        result = False
        while True:
            if self.area_left <= self.x and self.x <= self.area_right:
                if self.area_bottom <= self.y and self.y <= self.area_up:
                    result = True
                    break
            
            if self.x > self.area_right:
                break

            if self.y < self.area_bottom:
                break
            
            self.move()
        
        return result

    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        if self.v_x > 0:
            self.v_x -= 1
        self.v_y -= 1

if __name__ == '__main__':
    area_left, area_right = 57, 116
    area_up, area_bottom = -148, -198

    # highest = (1 + v_y) * v_y / 2
    # v_y + 1 <= 198
    # so v_y = 197
    # highest = (1 + 197) * 197 / 2 = 19503

    # v_x >= 11

    num = 0
    for i in range(11, 117):
        for j in range(-198, 198):
            s = Solution(i, j)
            if s.work():
                num += 1
    
    print(num)
