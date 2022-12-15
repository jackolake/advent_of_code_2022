import numpy as np
import scipy as sp
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Parse file
    with open('input/day12.txt', 'r') as f:
        inputs = [line.strip() for line in f.readlines()]

    # Parse input
    row_count, col_count = len(inputs), len(inputs[0])
    height_grid = np.zeros((row_count, col_count))
    start, end = (None, None), (None, None)
    for i, line in enumerate(inputs):
        for j, c in enumerate(line):
            height = {'S': 0, 'E': ord('z') - ord('a')}.get(c, ord(c) - ord('a'))
            height_grid[i][j] = height
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                end = (i, j)

    def run(part1=True):
        start_candidates = [start] if part1 else [(r, c) for r, c in np.argwhere(height_grid == 0)]
        # Construct graph
        g = nx.DiGraph()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(row_count):
            for col in range(col_count):
                for delta_row, delta_col in directions:
                    neighbour_row, neighbour_col = (row + delta_row), (col + delta_col)
                    # If neighbour does not go out of bound
                    if 0 <= neighbour_row < row_count and 0 <= neighbour_col < col_count:
                        # create a path if neighbour is at most 1 step higher than current node
                        if height_grid[neighbour_row][neighbour_col] - height_grid[row][col] <= 1:
                            g.add_edge((row, col), (neighbour_row, neighbour_col))
        # Return shortest path length
        distances = []
        for s in start_candidates:
            try:
                distances.append(nx.shortest_path_length(g, source=s, target=end, method='dijkstra'))
            except nx.NetworkXNoPath:
                pass
        return min(distances)


    # Part 1
    print(run(part1=True))
    # Part 2
    print(run(part1=False))
