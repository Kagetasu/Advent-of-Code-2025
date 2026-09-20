import time

def scan(matrix: list[str], remove=False):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    temp = matrix.copy()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '@':
                continue

            adj = 0
            # Top
            if i != 0:
                if matrix[i-1][j] == '@':
                    adj += 1

            # Top right
            if i != 0 and j != cols-1:
                if matrix[i-1][j+1] == '@':
                    adj += 1
    
            # Top left
            if i != 0 and j != 0:
                if matrix[i-1][j-1] == '@':
                    adj += 1

            # Left
            if j != 0:
                if matrix[i][j-1] == '@':
                    adj += 1

            # Right
            if j != cols - 1:
                if matrix[i][j+1] == '@':
                    adj += 1
            
            # Bottom
            if i != rows-1:
                if matrix[i+1][j] == '@':
                    adj += 1

            # Bottom right
            if i != rows-1 and j != cols-1:
                if matrix[i+1][j+1] == '@':
                    adj += 1

            # Bottom left
            if i != rows-1 and j != 0:
                if matrix[i+1][j-1] == '@':
                    adj += 1

            if adj < 4:
                count += 1
                if remove:
                    temp[i][j] = 'x'

    return count, temp

def part1(matrix: list[str]):
    count, _ = scan(matrix)
    return count

def part2(matrix: list[str]):
    total = 0
    count, temp = scan(matrix, remove=True)

    while count != 0:
        total += count
        count, temp = scan(temp, remove=True)
    
    return total

def main():
    with open('input.txt') as f:
        matrix = f.readlines()
        matrix = [list(x.strip()) for x in matrix]

    start = time.perf_counter()
    count = part1(matrix)
    end = time.perf_counter()
    print(f"Part 1: {count} | {end - start:.6f} seconds")

    start = time.perf_counter()
    count = part2(matrix)
    end = time.perf_counter()
    print(f"Part 2: {count} | {end - start:.6f} seconds")

main()