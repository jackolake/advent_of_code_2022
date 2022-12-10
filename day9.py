from collections import defaultdict
import numpy as np

if __name__ == '__main__':
    instructions = []
    # Parse file
    with open('input/day9.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                direction, num = line.split(' ')
                instructions.append((direction, int(num)))

    def run(knot_nums: int) -> int:
        knot_locations = np.zeros((knot_nums, 2))  # knot_locations[knot_number] = (x, y); knot #0 is Head
        tail_visited = defaultdict(int)

        for op, steps in instructions:
            axis = 0 if op in ('R', 'L') else 1
            step_delta = -1 if op in ('L', 'D') else 1
            for _ in range(steps):
                # Head move
                knot_locations[0][axis] += step_delta
                # Other knots follow
                for knot_idx in range(1, knot_nums):
                    delta_x = (knot_locations[knot_idx-1][0] - knot_locations[knot_idx][0])
                    delta_y = (knot_locations[knot_idx-1][1] - knot_locations[knot_idx][1])
                    if abs(delta_x) + abs(delta_y) > 2:
                        # Diagonal move if lagging too far behind
                        knot_locations[knot_idx][0] += delta_x / abs(delta_x)
                        knot_locations[knot_idx][1] += delta_y / abs(delta_y)
                    elif abs(delta_x) > 1:
                        # Horizontal move
                        knot_locations[knot_idx][0] += delta_x / abs(delta_x)
                    elif abs(delta_y) > 1:
                        # Vertical move
                        knot_locations[knot_idx][1] += delta_y / abs(delta_y)
                tail_visited[(knot_locations[knot_nums-1][0], knot_locations[knot_nums-1][1])] += 1
        return len(tail_visited.keys())

    # Part 1: 2 knots
    print(run(knot_nums=2))
    # Part 2: 10 knots
    print(run(knot_nums=10))
