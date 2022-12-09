if __name__ == '__main__':
    elf_pairs = []

    # Parse file
    with open('input/day4.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                elf_pair = []
                for pair in line.split(','):
                    start, end = pair.split('-')
                    elf_pair.append((int(start), int(end)))
                elf_pairs.append(elf_pair)


    def run(part1=True):
        count = 0
        for (elf1, elf2) in elf_pairs:
            (s1, e1), (s2, e2) = elf1, elf2
            if part1 and (s1 >= s2 and e1 <= e2 or s2 >= s1 and e2 <= e1) \
                    or ((not part1) and (s1 <= s2 <= e1 or s2 <= s1 <= e2)):
                count += 1
        return count


    # Part 1
    print(run(part1=True))
    # Part 2
    print(run(part1=False))
