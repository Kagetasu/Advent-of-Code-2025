def part1(ranges: list[str]):
    count = 0
    for r in ranges:
        l, h = [int(x) for x in r.split("-")]

        for i in range(l, h + 1):
            num = str(i)

            if len(num) % 2 != 0:
                continue
            if num[: int(len(num) / 2)] == num[int(len(num) / 2) :]:
                count += i

    return count


def part2(ranges: list[str]):
    count = 0
    invalid = set()
    for r in ranges:
        l, h = [int(x) for x in r.split("-")]

        for i in range(l, h + 1):
            num = str(i)

            size = 1
            while len(num) / size > 1:
                if num.count(num[:size]) == len(num) / size:
                    invalid.add(i)

                size += 1
    for num in invalid:
        count += num
    return count


def main():
    with open("input.txt") as f:
        ranges = f.readline().split(",")

    p1 = part1(ranges)
    print(f"Part 1: {p1}")

    p2 = part2(ranges)
    print(f"Part 2: {p2}")


main()
