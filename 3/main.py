import copy

def remove_element(strs, pos, one):
    output = []
    for str in strs:
        if one and str[pos] == '1':
            continue
        elif not one and str[pos] == '0':
            continue
        output.append(str)
    return output


if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        # question 1
        strs = []
        for line in f.readlines():
            strs.append(line.strip())
        
        length = len(strs[0])
        ones = [0] * length
        zeros = [0] * length
        for str in strs:
            for i in range(length):
                if str[i] == '1':
                    ones[i] += 1
                else:
                    zeros[i] += 1
        
        gamma = ''
        epsilon = ''
        for i in range(length):
            if ones[i] > zeros[i]:
                gamma += '1'
                epsilon += '0'
            else:
                gamma += '0'
                epsilon += '1'
        gamma_num = int(gamma, 2)
        epsilon_num = int(epsilon, 2)
 
        print(gamma, epsilon, gamma_num, epsilon_num, gamma_num * epsilon_num)


        # question 2
        strs_O2 = []
        for line in f.readlines():
            strs_O2.append(line.strip())
        strs_CO2 = copy.deepcopy(strs_O2)
        
        length = len(strs_O2[0])

        # O2
        for i in range(length):
            one, zero = 0, 0
            for str in strs_O2:
                if str[i] == '1':
                    one += 1
                else:
                    zero += 1
            if zero > one:
                strs_O2 = remove_element(strs_O2, i, True)
            else:
                strs_O2 = remove_element(strs_O2, i, False)
            if len(strs_O2) == 1:
                break
        
        # CO2
        for i in range(length):
            one, zero = 0, 0
            for str in strs_CO2:
                if str[i] == '1':
                    one += 1
                else:
                    zero += 1
            if zero > one:
                strs_CO2 = remove_element(strs_CO2, i, False)
            else:
                strs_CO2 = remove_element(strs_CO2, i, True)
            if len(strs_CO2) == 1:
                break
        
        print(strs_O2)
        print(strs_CO2)
        
        O2_num = int(strs_O2[0], 2)
        CO2_num = int(strs_CO2[0], 2)
 
        print(O2_num, CO2_num, O2_num * CO2_num)
