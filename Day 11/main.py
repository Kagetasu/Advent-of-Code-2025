import time
from functools import cache

def part1(devices: dict):
    total = 0
    def trace(start=str):
        if start == 'you':
            return 0
        if start == 'out':
            return 1
        
        return sum([trace(out) for out in devices[start]])
    
    total = sum([trace(out) for out in devices['you']])
    return total


def part2(devices: dict):
   
    @cache
    def count_paths(start, target):
       if start == target:
           return 1
       
       if start not in devices:
           return 0
       return sum(count_paths(s, target) for s in devices[start])
   
    p1 = count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')
    p2 = count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')

    return p1 + p2
    
    
def main():
    def parse_input(file: str):
        with open(file) as f:
            devices = {}
            for line in f.readlines():
                line = line.split(':')
                device = line[0]
                output = line[1].strip().split()
                devices[device] = output
        return devices
    
    devices = parse_input('input.txt')
    start = time.perf_counter()
    ans = part1(devices)
    end = time.perf_counter()
    print(f'Part 1: {ans} | {end - start:.6f} seconds')

    devices = parse_input('input.txt')
    start = time.perf_counter()
    ans = part2(devices)
    end = time.perf_counter()
    print(f'Part 2: {ans} | {end - start:.6f} seconds')

main()