def part1(lines: list):
    i = 50
    count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        if direction == "L":
            i -= distance
        else:
            i += distance

        i %= 100

        if i == 0:
            count += 1

    return count


def part2(lines: list):
    i = 50
    count = 0
    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        for _ in range(distance):
            if direction == "L":
                i -= 1
            else:
                i += 1

            i %= 100

            if i == 0:
                count += 1

    return count


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    p1 = part1(lines)
    print(f"Part 1: {p1}")

    p2 = part2(lines)
    print(f"Part 2: {p2}")


main()
