import sys

inputs = '''
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
'''

'''
l r
mjqjpqmgbljsphdztnvjfqwrcgsmlb
7 jpqm
19
bvwbjplbgvbhsrlpgdmjqwftvncz
5
23
nppdvjthqldpwncqszvftbrmjlhg
6
23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
10
29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
11
26
'''

inputs = inputs.strip()
# inputs = open('day_6.txt').read().strip()

# print(inputs)

def get_diff(inp):
    char = []
    char.append(inp[0])
    l = 0
    
    for i in range(len(inp) - 1):
        r = i+1
        if len(char) == 4:
            return r
        if inp[r] in char:
            idx = next((i for i, v in enumerate(char) if v == inp[r]), None)
            del char[:idx+1]
            l += 1
        char.append(inp[r])
    return 0

def get_diff_2(inp):
    char = []
    char.append(inp[0])
    l = 0
    for i in range(len(inp) - 1):
        r = i+1
        if len(char) == 14:
            return r
        if inp[r] in char:
            idx = next((i for i, v in enumerate(char) if v == inp[r]), None)
            del char[:idx+1]
            l += 1
        char.append(inp[r])
    return 0
            

if __name__ == "__main__":
    # res = get_diff(inputs)
    res = get_diff_2(inputs)

    print(res)