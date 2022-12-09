import re
from collections import defaultdict

if __name__ == '__main__':
    cranes_input = defaultdict(str)
    instructions = []

    # Parse file
    with open('input/day5.txt', 'r') as f:
        for line in f.readlines():
            line = line.replace('\r', '').replace('\n', '')
            if line:
                if '[' in line:
                    crane_count = int((len(line)+1)/4)
                    layer = [line[1 + i * 4] for i in range(crane_count)]
                    for i, crate in enumerate(layer):
                        cranes_input[i+1] += crate.replace(' ', '')
                elif 'move' in line:
                    instructions.append([int(num) for num in re.findall('\d+', line)])

    crane_count = len(cranes_input)

    def run(cranes, part1=True):
        for instruction in instructions:
            crate_num, from_crane, to_crane = instruction
            extract = cranes[from_crane][:crate_num]
            if part1:
                extract = extract[::-1]  # Order reversed in part 1
            cranes[from_crane] = cranes[from_crane][crate_num:]
            cranes[to_crane] = extract + cranes[to_crane]
        return ''.join([cranes[i+1][0] for i in range(crane_count)])

    # Part 1
    print(run(cranes_input.copy(), part1=True))
    # Part 2
    print(run(cranes_input.copy(), part1=False))
