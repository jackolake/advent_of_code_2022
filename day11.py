import numpy as np
from collections import defaultdict, deque
import re

if __name__ == '__main__':
    # Monkey config
    monkey_item_queue = defaultdict(deque)
    monkey_op = defaultdict(np.ufunc)
    monkey_op_value = defaultdict(int)
    monkey_test_value = defaultdict(int)
    monkey_test_true = defaultdict(int)
    monkey_test_false = defaultdict(int)

    # Parse file
    with open('input/day11.txt', 'r') as f:
        max_monkey_index = 0
        current_monkey = 0
        for line in f.readlines():
            line = line.strip()
            if line:
                if line.startswith('Monkey '):
                    current_monkey = int(re.findall('\d+', line)[0])
                elif 'Starting items: ' in line:
                    for item in re.findall('\d+', line):
                        monkey_item_queue[current_monkey].append(int(item))
                elif 'Operation: new = old' in line:
                    op, value = line.split(' ')[-2:]
                    monkey_op[current_monkey] = {'+': np.add, '*': np.multiply, '/': np.divide, '-': np.subtract}[op]
                    if op == '*' and value == 'old':  # new = old * old
                        monkey_op[current_monkey] = np.power
                        monkey_op_value[current_monkey] = 2
                    else:
                        monkey_op_value[current_monkey] = int(value)
                elif 'Test: divisible by ' in line:
                    monkey_test_value[current_monkey] = int(re.findall('\d+', line)[0])
                elif 'If true: throw to monkey' in line:
                    monkey_test_true[current_monkey] = int(re.findall('\d+', line)[0])
                elif 'If false: throw to monkey' in line:
                    monkey_test_false[current_monkey] = int(re.findall('\d+', line)[0])
                else:
                    raise RuntimeError('Invalid line: ' + line)
                max_monkey_index = max(max_monkey_index, current_monkey)

    def run(part1=True):
        rounds = 20 if part1 else 10000
        # Copy queue so it can run part 1 and part 2 without affecting each out
        item_queue = dict([(k, q.copy()) for k, q in monkey_item_queue.items()])
        # Tracker
        monkey_inspection = defaultdict(int)
        # For part 2: "gcd" to prevent worry value from overflowing yet preserve divisibility test
        gcd = np.prod([monkey_test_value[i] for i in range(max_monkey_index + 1)])
        for _ in range(rounds):
            for m_id in range(max_monkey_index + 1):
                q = item_queue[m_id]
                while q:
                    worry_item = q.popleft()
                    monkey_inspection[m_id] += 1
                    worry = monkey_op[m_id](worry_item, monkey_op_value[m_id])
                    bored = int(np.floor(worry / 3.0)) if part1 else worry % gcd
                    divisible_test = (bored % monkey_test_value[m_id]) == 0
                    item_queue[monkey_test_true[m_id] if divisible_test else monkey_test_false[m_id]].append(bored)
        # Result
        monkey_business = np.prod(sorted(list(monkey_inspection.values()), reverse=True)[:2])
        return monkey_business

    # Part 1
    print(run(part1=True))
    # Part 2
    print(run(part1=False))


