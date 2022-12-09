if __name__ == '__main__':
    datastream = ''

    # Parse file
    with open('input/day6.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                datastream = line

    def lookup(stream, length: int):
        for i in range(len(stream) - length + 1):
            if len(set(datastream[i:i + length])) == length:
                return i + length

    # Part 1
    print(lookup(datastream, length=4))
    # Part 2
    print(lookup(datastream, length=14))
