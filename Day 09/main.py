import time

def area(p1: tuple[int, int], p2: tuple[int, int]):
    length = abs(p1[1] - p2[1]) + 1
    width = abs(p1[0] - p2[0]) + 1

    return length*width

def part1(tiles: list[tuple[int, int]]):
    areas = []
    for t1 in tiles:
        for t2 in tiles:
            if t1 == t2:
                continue
            p1 = (int(t1[0]), int(t1[1]))
            p2 = (int(t2[0]), int(t2[1]))

            areas.append(area(p1, p2))

    return max(areas)
            

def print_grid(grid: list):
    for line in grid:
        print(' '.join(line))

def part2(tiles: list[tuple[int, int]]):
    L = len(tiles)
    grid_x = max(tiles, key=lambda t: int(t[0]))[0]+1
    grid_y = max(tiles, key=lambda t: int(t[1]))[1]+1

    #region Draw
    grid = [['.' for _ in range(grid_x)] for _ in range(grid_y)]
    
    for tile in tiles:
        x = tile[0]
        y = tile[1]
        grid[y][x] = '#'

    # Draw lines
    for i in range(L):
        curr = tiles[i]
        next_tile = tiles[(i+1)%L]
        # Adjacent on X
        if curr[1] == next_tile[1]:
            print(curr, next_tile)
            left = min(curr[0], next_tile[0])
            right = max(curr[0], next_tile[0])

            for j in range(left+1, right):
                grid[curr[1]][j] = 'X'

        #Adjacent on Y
        elif curr[0] == next_tile[0]:
            up = min(curr[1], next_tile[1])
            down = max(curr[1], next_tile[1])

            for j in range(up+1, down):
                grid[j][curr[0]] = 'X'

    queue = [(0,0)]
    visited = set([(0,0)])

    while queue:
        x, y = queue.pop(0)
        grid[y][x] = 'L'
    #endregion
    print_grid(grid)
    

def main():
    with open('sample.txt') as f:
        tiles = [(int(p[0]), int(p[1])) for p in (l.strip().split(',') for l in f.readlines())]
        
    start = time.perf_counter()
    ans = part1(tiles)
    end = time.perf_counter()
    print(f"Part 1: {ans} | {end - start:.6f} seconds")
    
    start = time.perf_counter()
    ans = part2(tiles)
    end = time.perf_counter()
    print(f"Part 2: {ans} | {end - start:.6f} seconds")

main()