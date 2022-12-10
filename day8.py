import numpy as np

if __name__ == '__main__':
    lines = []
    # Parse file
    with open('input/day8.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                lines.append(np.array([int(tree) for tree in line]))
    trees = np.asarray(lines)
    row_count, col_count = trees.shape

    # Part 1
    visible_trees = np.zeros(shape=trees.shape)
    for row in range(row_count):
        for col in range(col_count):
            # Either on boundary Or visible from any of West, East, North, South directions
            if row in (0, row_count - 1) or col in (0, col_count - 1) \
                    or trees[row, col] > max(trees[row, :col]) \
                    or trees[row, col] > max(trees[row, col+1:]) \
                    or trees[row, col] > max(trees[:row, col]) \
                    or trees[row, col] > max(trees[row+1:, col]):
                visible_trees[row, col] = 1
    print(visible_trees.sum())

    # Part 2
    def calc_score(line_of_sight: list, current_height: int):
        score = 0
        for height in line_of_sight:
            score += 1
            if height >= current_height:
                break  # Very tricky - Also counts the first tree with higher or same height to you
        return score

    scenic_scores = np.zeros(shape=trees.shape)
    for row in range(row_count):
        for col in range(col_count):
            my_height = trees[row, col]
            score_N = calc_score(trees[:row, col][::-1], my_height) if row > 0 else 0
            score_S = calc_score(trees[row+1:, col], my_height) if row < row_count - 1 else 0
            score_W = calc_score(trees[row, col+1:], my_height) if col < col_count - 1 else 0
            score_E = calc_score(trees[row, :col][::-1], my_height) if col > 0 else 0
            scenic_scores[row, col] = score_N * score_S * score_W * score_E
    print(scenic_scores.max())
