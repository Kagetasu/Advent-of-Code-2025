from itertools import product

def part1(machines: list[list]):
    total = 0
    for machine in machines:
        target = machine[0]

        nlight = len(machine[0])
        nbtn = len(machine[1])

        # Convert buttons to 0s and 1s
        buttons = [[0 for _ in range(nlight)] for _ in range(nbtn)]

        for i in range(nbtn):
            for b in machine[1][i]:
                buttons[i][b] = 1
        #################################

        # Build matrix
        matrix = []
        for r in range(nlight):
            row = []
            for c in range(nbtn):
                row.append(buttons[c][r])
            row.append(target[r])
            matrix.append(row)
        #################################
        
        # Gaussian Elimination
        pivot_row = 0
        pivot_cols = {}
        free_vars = []
        
        for col in range(nbtn):
            if pivot_row >= nlight:
                free_vars.append(col)
                continue
            
            selected_row = -1
            for r in range(pivot_row, nlight):
                if matrix[r][col] == 1:
                    selected_row = r
                    break
            
            if selected_row == -1:
                free_vars.append(col)
                continue

            matrix[pivot_row], matrix[selected_row] = matrix[selected_row], matrix[pivot_row]
            pivot_cols[col] = pivot_row

            for r in range(nlight):
                if r != pivot_row and matrix[r][col] == 1:
                    for c in range(col, nbtn+1):
                        matrix[r][c] ^= matrix[pivot_row][c]

            pivot_row += 1

        min_presses = float('inf')

        for free_vals in product([0, 1], repeat=len(free_vars)):
            solution = [0] * nbtn
            current_presses = 0

            for i, fv in enumerate(free_vars):
                val = free_vals[i]
                solution[fv] = val
                current_presses += val

            for col in range(nbtn - 1, -1, -1):
                if col in pivot_cols:
                    r = pivot_cols[col]
                    val = matrix[r][-1]

                    for check in range(col + 1, nbtn):
                        if matrix[r][check] == 1:
                            val ^= solution[check]
                    

                    solution[col] = val
                    current_presses += val

            if current_presses < min_presses:
                min_presses = current_presses

        total += min_presses
        
    return total
        

def part2():
    pass

def main():
    with open('input.txt') as f:
        machines = []
        for line in f.readlines():
            l = line.strip().split()
            target = [1 if x == '#' else 0 for x in list(l[0][1:-1])]
            buttons = [tuple([int(x) for x in button[1:-1].split(',')]) for button in l[1:-1]]
            joltage = [int(x) for x in l[-1][1:-1].split(',')]
            machines.append((target, buttons , joltage))
        
    
    total = part1(machines)
    print(f'Part 1: {total}')

main()