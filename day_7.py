import sys 
from collections import defaultdict, deque

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
# inputs = open('day_7.txt').read().strip().split('\n')

# print(inputs)


def test(folders):
    test_sentence = 'test not passed 4 sub folders'
    if len(folders) < 4:
        print(test_sentence, len(folders))
    else:
        print('test passed with 4 sub folders')

def parse(inp):
    filtered_inp = []
    for i, line in enumerate(inp):
        if '$ ls' not in line and '$ cd ..' not in line:
            filtered_inp.append(line)
    inp = filtered_inp

    folders = defaultdict(list)
    name = None
    for i, line in enumerate(inp):
        if 'cd' in line:
            name = line.split(' ')[-1]
            folders[name] = []
        elif 'dir' in line:
            sub_folder = line.split(' ')[-1]
            folders[name].append(sub_folder)
        elif line[0].isdigit():
            num, _ = line.split(' ')
            num = int(num)
            folders[name].append(num)

    return folders

def bfs(graph):
    print(graph)
    total = 0
    start = '/'
    visited = set()
    queue = deque()

    queue.append(start)

    while queue:
        key = queue.popleft()
        if key not in visited:
            visited.add(key)

            for neighbor in graph[key]:
                if neighbor not in visited:
                    print(neighbor)
                    queue.append(neighbor)



def get_res(inp):
    folders = parse(inp)
    test(folders)
    total = bfs(folders)

if __name__ == "__main__":
    res = get_res(inputs)
    print(res)







