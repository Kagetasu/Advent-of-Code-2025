import time
import random

# Rotates NxN grid
def rotate(grid):
    return [
        "".join(grid[len(grid) - 1 - r][c] for r in range(len(grid)))
        for c in range(len(grid[0]))
    ]

# Mirrors NxN grid
def flip(grid):
    return [row[::-1] for row in grid]

# Result in all orientations of the shape in x, y coords
def orientations(shape):
    seen, res = set(), []
    for flip_flag in (False, True):
        base = flip(shape) if flip_flag else shape
        cur = base
        for k in range(4):
            if k > 0:
                cur = rotate(cur)
            key = "\n".join(cur)

            if key not in seen:
                seen.add(key)
                cells = [
                    (r, c)
                    for r, row in enumerate(cur)
                    for c, ch in enumerate(row)
                    if ch == "#"
                ]
                res.append((cells, len(cur), len(cur[0])))
    return res

# Returns if shapes fit in an NxN grid or not
def packable(width, height, counts, shape_orients, shape_area, attempts=10):
    # If the area of the presents is bigger than the grid -> False
    total = sum(c * a for c, a in zip(counts, shape_area))
    if total > width * height:
        return False
    
    # What shapes are we trynna fit
    pieces = []
    for i, cnt in enumerate(counts):
        pieces.extend([i] * cnt)

    # Start with largest first cuz they're hardest to fit later on
    pieces.sort(key=lambda i: shape_area[i], reverse=True)
    for _ in range(attempts):
        # NxN board of False (False means no #)
        board = [[False] * width for _ in range(height)]
        ok = True

        for p in pieces:
            placed = False

            # Shuffle orientations and try each
            for cells, hh, ww in random.sample(shape_orients[p], len(shape_orients[p])):
                
                for y in range(height - hh + 1):
                    if placed: 
                        break

                    for x in range(width - ww + 1):
                        # Collision check
                        if any(board[y + dr][x + dc] for dr, dc in cells):
                            continue

                        # Place
                        for dr, dc in cells:
                            board[y + dr][x + dc] = True

                        placed = True
                        break

                if placed:
                    break

            if not placed:
                ok = False
                break
        if ok:
            return True
        
    return False

def part1(shapes: list[str], regions: list[str]):
    shape_area = [sum(row.count("#") for row in s) for s in shapes]
    shape_orients = [orientations(s) for s in shapes]

    results = []
    for line in regions:
        dimensions, pieces = line.split(":")
        width, height = map(int, dimensions.split("x"))
        counts = list(map(int, pieces.split()))
        results.append(packable(width, height, counts, shape_orients, shape_area))

    return results

def main():
    start = time.perf_counter()

    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        shapes = []
        for i in range(0, len(lines), 5):
            if "x" not in lines[i]:
                shapes.append(lines[i + 1 : i + 4])
            else:
                regions = lines[i:]
                break
    
    
    results = part1(shapes, regions)
    end = time.perf_counter()
    print(f"Part 1: {sum(results)} | {end - start:.6f} seconds")


main()
