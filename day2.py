if __name__ == '__main__':
    opponent_symbols = []
    your_symbols = []

    # Parse file
    with open('input/day2.txt', 'r') as f:
        calories = []
        for line in f.readlines():
            line = line.strip()
            if line:
                opponent, you = line.split(' ')
                opponent_symbols.append(opponent)
                your_symbols.append(you)

    def run_game(part1=True):
        scores = 0
        for opp_sym, your_sym in zip(opponent_symbols, your_symbols):
            oppo_score = ord(opp_sym) - ord('A') + 1
            # Logic interpretation
            if part1:
                your_score = ord(your_sym) - ord('X') + 1
            else:
                your_score = {
                    'X': (oppo_score - 2) % 3 + 1,      # Lose  2 => 1
                    'Y': oppo_score,                    # Draw
                    'Z': (oppo_score % 3) + 1,          # Win
                }[your_sym]
            # Common score logic
            if (your_score - oppo_score) % 3 == 1:  # Win
                scores += 6
            elif your_score == oppo_score:  # Draw
                scores += 3
            scores += your_score
        return scores

    # Part 1
    print(run_game(part1=True))
    # Part 2
    print(run_game(part1=False))
