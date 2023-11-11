import sys 

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
95437 (94853 + 584) < 100000

                    /
        a               14848514   8504156          d
    a 29116 2557 62596                      4060174 8033020 5626152 7214296
584

cd ..
7214296 d 584 a 62596 2557 29116 a d 8504156 14848514 a /

base case:
recursion: 
'''



# inputs = inputs.strip().split('\n')
inputs = open('day_7.txt').read().strip().split('\n')

inputs = [line for line in inputs if '$ ls' not in line and '$ cd ..' not in line]

# with open('test.txt', 'w') as output:
#     output.write('\n'.join(inputs))

# print(inputs)

def test():
    test_tar = 'tbj'
    failure = 'test not passed '
    success = 'test passed '
    for line in inputs:
        if test_tar in line:
            print(line)




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
    
    

def recursive(r, bucket, dir_folders, cd_folders, total):
    threshold = 100000
    sub_sum = 0

    # dir: [wtmcqwgp, tbj, mdh, hzl]
    # cd: [tbj, stcgrs, wtmcqwgp, tbj, mdh, hzl]

    print('line, bucket', r, bucket)

    if r > 0:
        while not '$ cd' in inputs[r]:
            val = parse(inputs[r])
            print('val', val, inputs[r])
            if not isinstance(val, int):
                print('bucket val pop', val, bucket[val], dir_folders, cd_folders)
                l = r + 1
                dir_folders.append(val)
                if l:
                    cd_next = cd_folders[cd_folders.index(val) + 1]
                    dir_next = dir_folders[dir_folders.index(val) + 1]
                    if dir_next == cd_next:
                        val = bucket.pop(val, None)
                else:
                    val = bucket.pop(val, None)
            sub_sum += val
            r -= 1
        key = parse(inputs[r])
        cd_folders.append(key)
        if sub_sum < threshold:
            total += sub_sum
            print('new total', sub_sum, total)
        bucket[key] = sub_sum
        r -= 1
        recursive(r, bucket, dir_folders, cd_folders, total)
    else:
        print('final', total)
        return total
        

def get_res():
    last = len(inputs) - 1
    dir_folders = []
    cd_folders = []
    bucket = {}
    total = 0
    
    total = recursive(last, bucket, dir_folders, cd_folders, total)
    return total

if __name__ == '__main__':
    res = get_res()
    print(res)

    test()

