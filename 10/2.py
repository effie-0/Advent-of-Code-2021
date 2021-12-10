if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        scores = []
        incompletes = []
        
        for line in f.readlines():
            content = line.strip()

            stack = []
            end = False
            score = 0
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
                        break
            
            if not end and len(stack):
                for ch in reversed(stack):
                    score *= 5
                    if ch == '(':
                        score += 1
                    elif ch == '[':
                        score += 2
                    elif ch == '{':
                        score += 3
                    else:
                        score += 4

                scores.append(score)
        
        scores = sorted(scores)
        mid = int(len(scores) / 2)
        print(scores, scores[mid])
