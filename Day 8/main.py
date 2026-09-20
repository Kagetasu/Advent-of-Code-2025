import time
import math
from collections import Counter

def part1(boxes: list[list[str, int]]):
    L = len(boxes)
    
    adj = []

    for x in range(L):
        for y in range(x+1, L):
            d = math.dist(boxes[x][0], boxes[y][0])     
            adj.append((x,y,d))

    adj.sort(key=lambda p: p[2])
    
    r = 1000 if L == 1000 else 10
    for x, y, _ in adj[:r]:
        c_x, c_y = boxes[x][1], boxes[y][1]
        if c_x == c_y:
            continue
        
        
        for box in boxes:
            if box[1] == c_y:
                box[1] = c_x

    counts = Counter(b[1] for b in boxes)
    circuits = sorted(counts.values(), reverse=True)
    total = circuits[0] * circuits[1] * circuits[2]
    return total
        

def part2(boxes: list[list[str, int]]):
    L = len(boxes)
    
    adj = []

    for x in range(L):
        for y in range(x+1, L):
            d = math.dist(boxes[x][0], boxes[y][0])     
            adj.append((x,y,d))

    adj.sort(key=lambda p: p[2])
    
    
    for x, y, _ in adj:
        c_x, c_y = boxes[x][1], boxes[y][1]
        if c_x == c_y:
            continue
        
        
        for box in boxes:
            if box[1] == c_y:
                box[1] = c_x

        mul = boxes[x][0][0] * boxes[y][0][0]

    return mul

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        boxes = []
        for i, l in enumerate(lines):
            boxes.append([[int(x) for x in l.strip().split(',')], i]) # [box, circuit]

    start = time.perf_counter()
    total = part1(boxes)
    end = time.perf_counter()
    print(f"Part1: {total} | {end-start:.6f} seconds")

    start = time.perf_counter()
    total = part2(boxes)
    end = time.perf_counter()
    print(f"Part2: {total} | {end-start:.6f} seconds")

main()