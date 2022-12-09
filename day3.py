from collections import defaultdict
from itertools import zip_longest

if __name__ == '__main__':
    backpacks = []

    # Parse file
    with open('input/day3.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                backpacks.append(line)

    def calc_priority(c: str) -> int:
        if c.islower():
            return ord(c) - ord('a') + 1
        return ord(c) - ord('A') + 27

    def find_collision(compartments: list) -> int:
        counter = defaultdict(int)
        for compartment in compartments:
            for item in set(compartment):
                counter[item] += 1
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return sorted_counter[0][0]

    def run(part1=True):
        priority_total = 0
        if part1:
            # For each elf, find collision between 2 halves of the backpack
            iterator = [[b[:int(len(b)/2)], b[int(len(b)/2):]] for b in backpacks]
        else:
            # For every 3 elves, find collision between each backpack
            iterator = zip_longest(*[iter(backpacks)] * 3)
        for i in iterator:
            collision = find_collision(i)
            priority = calc_priority(collision)
            priority_total += priority
        return priority_total

    # Part 1
    print(run(part1=True))
    # Part 2
    print(run(part1=False))
