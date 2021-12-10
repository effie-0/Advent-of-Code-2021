if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        score = 0
        for line in f.readlines():
            content = line.strip()

            stack = []
            end = False
            end_ch = ''
            for ch in content:
                if ch in '([{<':
                    stack.append(ch)
                else:
                    if len(stack) == 0:
                        end = True
                    
                    left = stack.pop()
                    if ch == ')' and left != '(':
                        end = True
                    elif ch == ']' and left != '[':
                        end = True
                    elif ch == '}' and left != '{':
                        end = True
                    elif ch == '>' and left != '<':
                        end = True
                    
                    if end:
                        end_ch = ch
                        break
            
            if len(end_ch) > 0:
                if end_ch == ')':
                    score += 3
                elif end_ch == ']':
                    score += 57
                elif end_ch == '}':
                    score += 1197
                else:
                    score += 25137
        
        print(score)
