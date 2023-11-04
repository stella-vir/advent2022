import sys 
from collections import defaultdict

inputs = '''
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
$ cd / $ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e '' cd ..
{a: e, f, g, h}


584 + 94853 -f (size 29116), g (size 2557), and h.lst (size 62596), plus file i(584) + 24933642 = 48381165
95437 (94853 + 584) < 100000
'''
inputs += '$ ls'

inputs = inputs.strip().split('\n')
# input = open('day_7.txt').read().strip().split('\n')

# print(inputs)


def test(inp):
    test_sentence = 'not passed'
    dirs = defaultdict(list)
    sub_total = 0
    threshold = 100000

    l = 0
    for i in range(len(inp)-1):
        r = i+1
        if '$ cd' in inp[l]:
            _, _, dir_name = inp[l].split(' ')
            if inp[r].startswith('dir'):
                _, name = inp[r].split(' ')
                dirs[dir_name].append(name)
            if inp[r][0].isdigit():
                num, _ = inp[r].split(' ')
                sub_total += int(num)
                dirs[dir_name].append(sub_total)
                sub_total = 0
                if '$ cd' in inp[r]:
                    l = r
                    r += 1
    if len(dirs) < 4:
        print(test_sentence, 'not 4 sub dirs', len(dirs))

def parse(inp):
    pass

def get_total(dirs):
    pass


def get_res(inp):
    dirs = parse(inp)
    total = get_total(dirs)

    return total

if __name__ == "__main__":
    test(inputs)
    
    # res = get_res(input)
    # print(res)






