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
dir a
29116 f
2557 g
62596 h.lst
$ cd a
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
584 + 94853 -f (size 29116), g (size 2557), and h.lst (size 62596), plus file i(584) + 24933642 = 48381165
-> 95437 (94853 + 584) < 100000

/-a 94853+584
/-a-a 584
/-d 24933642

cd ..
7214296 d 584 a 62596 2557 29116 a d 8504156 14848514 a /

base case:
recursion:
-> 1243729

> 30000000 - (70000000 - 48381165) = 8381165
-> d 24933642
> 30000000 - (70000000 - total/44376732) = 4376732
-> 4443914
'''


# inputs = inputs.strip().split('\n')
inputs = open('day_7.txt').read().strip().split('\n')

# part1
# inputs = [line for line in inputs if '$ ls' not in line and '$ cd ..' not in line]

# part2
inputs = [line for line in inputs if '$ ls' not in line and 'dir' not in line]

# with open('test.txt', 'w') as output:
#     output.write('\n'.join(inputs))

# print(inputs)

def test():
    test_tar = 'tbj'
    failure = 'test not passed '
    success = 'test passed '
    add_up = 0
    for line in inputs:
        if test_tar in line and '$ cd' not in line:
            # print(line)
            if line[0].isdigit():
                num, _ = line.split(' ')
                add_up += int(num)
    #! print('add up', add_up)


def parse(line):
    if '$ cd' in line:
        _, _, sub_folder = line.split(' ')
        return sub_folder
    elif 'dir' in line:
        _, sub_dir = line.split(' ')
        return sub_dir
    elif line[0].isdigit():
         num, _ = line.split(' ')
         num = int(num)
         return num 
    
    

def recursive(r, bucket, total):
    threshold = 100000
    sub_sum = 0

    if r > 0:
        while not '$ cd' in inputs[r]:
            val = parse(inputs[r])
            if not isinstance(val, int):
                val = bucket[val]
            sub_sum += val
            r -= 1
        key = parse(inputs[r])
        if sub_sum < threshold:
            total += sub_sum
        bucket[key] = sub_sum
        r -= 1
        recursive(r, bucket, total)
    else:
        print('final', total)
        return total
        

def get_res():
    last = len(inputs) - 1
    bucket = {}
    total = 0
    
    total = recursive(last, bucket, total)
    return total


def arr_dict_2(inp):
    bucket = []
    folders = defaultdict(int)

    for line in inp:
        if '$ cd' in line:
            if '..' in line:
                bucket.pop()
            else:
                sub = parse(line)
                bucket.append(sub)
        else:
            num = parse(line)
            num = int(num)
            for i in range(1, len(bucket) + 1):
                key = '/'.join(bucket[:i])
                folders[key] += num

    return folders

    

def get_res_2(inp):
    least = 99999999

    folders = arr_dict_2(inp)
    
    # total = folders['/']
    total = 0
    for line in inp:
        if line[0].isdigit():
            total += parse(line)

    print('total', total)
    
    to_delete = 30000000 - (70000000 - total)
    print('to delete', to_delete)

    for k, v in folders.items():
        if v > to_delete:
            least = min(least, v)

    return least


if __name__ == '__main__':
    # res = get_res()
    # print(res)

    # test()

    res_2 = get_res_2(inputs)
    print(res_2)


