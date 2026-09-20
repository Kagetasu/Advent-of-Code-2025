import time
import queue
from functools import cache

def part1(graph: list[str], start: int):
    total = 0
    visited = set()
    beams = queue.Queue()
    beams.put([0, start])

    while not beams.empty():
        b = beams.get()

        while b[0] < len(graph)-1:
            graph[b[0]][b[1]] = '|'
            if graph[b[0]+1][b[1]] == '^':
                
                if (b[0]+1, b[1]) not in visited:
                    total += 1
                    
                    if [b[0]+1, b[1]-1] not in beams.queue:
                        beams.put([b[0]+1, b[1]-1]) # Beam left
                    if [b[0]+1, b[1]+1] not in beams.queue:
                        beams.put([b[0]+1, b[1]+1]) # Beam right

                    visited.add((b[0]+1, b[1]))
                break

            else:
                b[0] +=1
    
    return total


def part2(graph: list[list[str]], start):
    H = len(graph)

    @cache
    def count_paths(x, y):
        if y == H - 1:
            return 1
        
        if graph[y+1][x] == '^':
            return count_paths(x-1, y+1) + count_paths(x+1, y+1)
        else:
            return count_paths(x, y+1)
        
    return count_paths(start, 0)

def main():

    with open('input.txt') as f:
        lines = [list(l.strip()) for l in f.readlines()]
        s = lines[0].index('S')

    start = time.perf_counter()
    total = part1(lines, s)
    end = time.perf_counter()
    print(f"Part 1: {total} | {end - start:.6f} seconds")

    start = time.perf_counter()
    total = part2(lines, s)
    end = time.perf_counter()
    print(f"Part 2: {total} | {end - start:.6f} seconds")

main()