import sys 

input = '''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

'''
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..

584 + 94853 -f (size 29116), g (size 2557), and h.lst (size 62596), plus file i(584) + 24933642 = 48381165
95437 (94853 + 584) < 100000
'''

# input = input.strip().split('\n')
input = open('day_7.txt').read().strip().split('\n')

def parse(inp):
    between_ls = False
    dirs = []

    for i, line in enumerate(inp):
        if 'dir' in line:
            _, level = line.split(' ')
            dirs.append(level)
        elif line[0].isdigit():
            size, key = line.split(' ')
            size = int(size)
            if size < 100000:
                if 'ls' in input[i-1]:
                    dirs.append((key, size))
                else:
                    dirs.append(size)
    return dirs

def get_total(dirs):
    print(dirs)
    total_arr = []
    sub_total = 0
    total = 0

    for val in dirs:
        if isinstance(val, int):
            sub_total += val
        elif isinstance(val, tuple):
            sub_dir = val[1]
            sub_total += sub_dir
            total_arr.append(sub_dir)
        else:
            if sub_total != 0:
                total_arr.append(sub_total)
            sub_total = 0
            
    if sub_total != 0:
        total_arr.append(sub_total)
    
    print(total_arr)

    total_arr = [val for val in total_arr if val < 100000]

    for t in total_arr:
        total += t

    print(total)

    return total


def get_res(inp):
    dirs = parse(inp)
    total = get_total(dirs)

    return total

if __name__ == "__main__":
    res = get_res(input)
    print(res)





