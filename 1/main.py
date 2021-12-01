if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1
        count = 0
        prev = -1
        for line in f.readlines():
            number = int(line.strip())
            if number > prev:
                count += 1
            prev = number
        print(count - 1)

        # question 2
        count = 0
        window = []
        prev = 0
        summ = 0
        for line in f.readlines():
            number = int(line.strip())
            if len(window) < 3:
                window.append(number)
                summ += number
            else:
                prev = summ
                summ = summ - window[0] + number
                window = window[1:]
                window.append(number)
                if summ > prev:
                    count += 1
        print(count)
