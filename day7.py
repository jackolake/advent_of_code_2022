from collections import defaultdict

if __name__ == '__main__':
    current_dir_tokens = ['']  # '/abc/def'.split('/') => ['', 'abc', 'def']
    directory_size_dict = defaultdict(int)
    file_size_dict = dict()

    # Parse file
    with open('input/day7.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                if line.startswith('$'):
                    # Process commands
                    if line.startswith('$ cd'):  # '$ ls' itself does not carry information
                        cd = line.split(' ')[-1]
                        if cd == '..':
                            current_dir_tokens.pop()
                        elif cd == '/':
                            current_dir_tokens = ['']
                        else:
                            current_dir_tokens.append(cd)
                else:
                    current_dir = '/'.join(current_dir_tokens)
                    file_or_dir_path = current_dir + '/' + line.split(' ')[-1]
                    if line.startswith('dir'):
                        directory_size_dict[file_or_dir_path] += 0
                    else:
                        file_size = int(line.split(' ')[0])
                        if file_or_dir_path not in file_size_dict:
                            file_size_dict[file_or_dir_path] = file_size
                            for i in range(len(current_dir_tokens)):
                                sub_folder_path = '/'.join(current_dir_tokens[:i+1])
                                directory_size_dict[sub_folder_path] += file_size

    # Part 1 - Sum of sizes of directories less than size 100000
    print(sum([size for folder, size in directory_size_dict.items() if size <= 100000]))

    # Part 2 - Total Size: 70000000, Need min space 30000000, Find minimum directory size to free up
    free_space = 70000000 - directory_size_dict['']
    required_space = 30000000 - free_space
    print(min([size for folder, size in directory_size_dict.items() if size >= required_space]))

