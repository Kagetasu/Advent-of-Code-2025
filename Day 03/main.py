import time

def part1(banks: list[list[int]]):
    total = 0

    for bank in banks:
        a = max(bank[:-1])
        i = bank.index(a)
        b = max(bank[i+1:])

        total += int(str(a) + str(b))
    
    return total

def part2(banks: list[list[int]]):
    total = 0

    for bank in banks:
        i, j = -1, -11
        num = ""
        
        for d in range(12):
            if d == 11:
                m = max(bank[i+1:])
            else:
                m = max(bank[i+1:j])
                
            num += str(m)
            
            if d != 11:
                i += bank[i+1: j].index(m) + 1
                j += 1

        total += int(num)
    
    return total

def main():
    with open('input.txt') as f:
        banks = [[int(x) for x in l.strip()] for l in f.readlines()]
    
    start = time.perf_counter()
    total = part1(banks)
    end = time.perf_counter()
    print(f"Part 1: {total} | {end - start:.6f} seconds")

    start = time.perf_counter()
    total = part2(banks)
    end = time.perf_counter()
    print(f"Part 2: {total} | {end - start:.6f} seconds")

main()