import time

def part1(ranges: list[tuple], ingredients: list[str]):
    count = 0

    for ingredient in ingredients:
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                count += 1
                break

    return count
    
def part2(ranges: list[tuple]):
    ranges.sort(key=lambda r: (r[0], r[1]))
    count = 0
    
    prev_min = ranges[0][0]
    prev_max = ranges[0][1]
    for i, r in enumerate(ranges):
        if i == 0:
            continue
        
        start, end = r

        if start > prev_max:
            count += prev_max - prev_min + 1

            prev_min = start
            prev_max = end
        
        else:
            prev_max = max(prev_max, end)
    
    count += prev_max - prev_min + 1
    
    return count

def main():
    with open('input.txt') as f:
        lines = f.readlines()
        i = lines.index("\n")
        
        ranges = [(int(x), int(y)) for line in lines[:i] for x,y in [line.strip().split('-')]]
        ingredients = [int(x) for x in lines[i+1:]]

    start = time.perf_counter()
    count = part1(ranges, ingredients)
    end = time.perf_counter()
    print(f"Part 1: {count} | {end - start:.6f} seconds")

    start = time.perf_counter()
    count = part2(ranges)
    end = time.perf_counter()
    print(f"Part 2: {count} | {end - start:.6f} seconds")

main()