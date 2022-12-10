import numpy as np

if __name__ == '__main__':
    # Parse file
    with open('input/day10.txt', 'r') as f:
        instructions = [line.strip() for line in f.readlines()]

    total_cycles = sum([{'noop': 1}.get(i, 2) for i in instructions])
    x = np.ones((total_cycles + 1, 2))  # x[cycle][0] = x_start; x[cycle][1] = x_end
    cycle = 1
    for instruction in instructions:
        if instruction == 'noop':
            x[cycle][0] = x[cycle - 1][1]
            x[cycle][1] = x[cycle - 1][1]
            cycle += 1
        else:
            add_x = int(instruction.split(' ')[-1])
            x[cycle][0] = x[cycle - 1][1]
            x[cycle][1] = x[cycle - 1][1]
            x[cycle + 1][0] = x[cycle - 1][1]
            x[cycle + 1][1] = x[cycle - 1][1] + add_x
            cycle += 2

    # Part 1
    print(sum([cycle * x[cycle][0] for cycle in [20, 60, 100, 140, 180, 220]]))

    # Part 2
    drawing = ''
    for cycle in range(1, 241):
        cycle_position = (((cycle-1) % 40) + 1)
        if x[cycle][0] <= cycle_position <= x[cycle][0] + 2:
            drawing = drawing + '#'
        else:
            drawing = drawing + ' '
    for i in range(6):
        print(drawing[i*40: i*40 + 40])  # FZBPBFZF
