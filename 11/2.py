def flash(energies, m, n, i, j):
    if energies[i][j] == -1:
        return
    
    energies[i][j] += 1
    if energies[i][j] > 9:
        energies[i][j] = -1
        spread(energies, m, n, i, j)


def spread(energies, m, n, i, j):
    if i > 0:
        if j > 0:
            flash(energies, m, n, i - 1, j - 1)

        flash(energies, m, n, i - 1, j)

        if j < n - 1:
            flash(energies, m, n, i - 1, j + 1)
    
    if j > 0:
        flash(energies, m, n, i, j - 1)
    
    if j < n - 1:
        flash(energies, m, n, i, j + 1)
    
    if i < m - 1:
        if j > 0:
            flash(energies, m, n, i + 1, j - 1)
        
        flash(energies, m, n, i + 1, j)

        if j < n - 1:
            flash(energies, m, n, i + 1, j + 1)


def one_step(energies, m, n):
    for i in range(m):
        for j in range(n):
            flash(energies, m, n, i, j)
    
    num = 0
    for i in range(m):
        for j in range(n):
            if energies[i][j] == -1:
                num += 1
                energies[i][j] = 0
    
    return num

if __name__ == '__main__':
    with open('./input.txt', 'r') as f:
        energies = []
        for line in f.readlines():
            content = [int(x) for x in line.strip()]
            energies.append(content)

    steps = 0
    m = len(energies)
    n = len(energies[0])
    while True:
        steps += 1
        flash_num = one_step(energies, m, n)
        if flash_num == m * n:
            break

    print(steps)
