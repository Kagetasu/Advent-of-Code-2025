import time

def part1(operands, operators):
    total = 0

    for y in range(len(operands[0])):
        result = int(operands[0][y])
        for x in range(1, len(operands)):
        
            if operators[y] == '+':
                result += int(operands[x][y])
            else:
                result *= int(operands[x][y])
            
            
        total += result
    
    return total

def part2(operands, operators):
    total = 0

    for y in range(len(operands[0])):
        new_operands = ["" for _ in range(len(operands))]
        for x in range(len(operands)):
            for i, c in enumerate(operands[x][y]):
                new_operands[i] += c

        result = int(new_operands[0])
        
        for op in new_operands[1:]:
            if not op.strip(): 
                continue

            if operators[y] == '+':
                result += int(op)
            else:
                result *= int(op)

            
        total += result


    return total              

def max_col_len(lines: list[str]):
    copy_lines = [l.split() for l in lines]
    ncols = len(copy_lines[0])
    
    columns = [[] for _ in range(ncols)]
    for x in range(len(copy_lines)):
        for y in range(ncols):
            columns[y].append(copy_lines[x][y])
            
    widths = [len(str(max([int(x) for x in columns[i]]))) for i in range(ncols)]
    
    return widths


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        operators = lines[-1].split()
        
        operands = [[] for _ in range(len(lines)-1)]
        
        col_widths = max_col_len(lines[:-1])

        for y, line in enumerate(lines[:-1]):
            j = 0
            for w in col_widths:
                operands[y].append(line[j:j+w])
                j += w + 1   
    
   

    start = time.perf_counter()
    total = part1(operands, operators)
    end = time.perf_counter()
    print(f"Part 1: {total} | {end - start:.6f} seconds")

    start = time.perf_counter()
    total = part2(operands, operators)
    end = time.perf_counter()
    print(f"Part 2: {total} | {end - start:.6f} seconds")

main()