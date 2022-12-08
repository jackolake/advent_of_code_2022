import numpy as np

if __name__ == '__main__':
    elf_foods = []
    elf_idx = 0
    # Parse file
    with open('input/day1.txt', 'r') as f:
        calories = []
        for line in f.readlines():
            line = line.strip()
            if line:
                num = int(line)
                calories.append(num)
            else:
                elf_foods.append(calories)
                calories = []
                elf_idx += 1

    # Common
    elf_calories = [sum(e) for e in elf_foods]
    # Part 1
    part1 = max(elf_calories)
    print(part1)

    # Part 2
    part2 = sum(sorted(elf_calories, reverse=True)[:3])
    print(part2)
