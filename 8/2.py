def line_process(ins, outs):
    mapping = [''] * 10
    remain = []
    for val in ins:
        content = ''.join(sorted(val))
        if len(val) == 2:
            mapping[1] = content
        elif len(val) == 4:
            mapping[4] = content
        elif len(val) == 3:
            mapping[7] = content
        elif len(val) == 7:
            mapping[8] = content
        else:
            remain.append(content)
    
    five_or_six = []
    two = []
    temp = []
    for val in remain:
        if mapping[1][0] not in val:
            five_or_six.append(val)
        elif mapping[1][1] not in val:
            two.append(val)
        else:
            temp.append(val)
    
    remain = temp
    
    if len(five_or_six) < len(two):
        temp = two
        two = five_or_six
        five_or_six = temp

    mapping[2] = two[0]
    if len(five_or_six[0]) == 5:
        mapping[5] = five_or_six[0]
        mapping[6] = five_or_six[1]
    else:
        mapping[6] = five_or_six[0]
        mapping[5] = five_or_six[1]

    for val in remain:
        if len(val) == 5:
            mapping[3] = val
            remain.remove(val)
            break

    for val in remain:
        contain = True
        for ch in mapping[4]:
            if ch not in val:
                contain = False
                break
        
        if contain:
            mapping[9] = val
        else:
            mapping[0] = val
    
    # convent to dict
    dictionary = {}
    for i in range(len(mapping)):
        dictionary[mapping[i]] = i
    
    # output
    output = 0
    for val in outs:
        content = ''.join(sorted(val))
        output = output * 10 + dictionary[content]
    
    return output


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        summ = 0
        for line in f.readlines():
            content = line.strip().split(' | ')
            ins = content[0].split()
            outs = content[1].split()
            summ += line_process(ins, outs)
        print(summ)
