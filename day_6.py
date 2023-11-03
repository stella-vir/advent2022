import sys

input = '''
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

# input = input.strip()
input = open('day_6.txt').read().strip()

# print(input)

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
            
# res = get_diff(input)
# print(res)

def get_diff_2(inp):
    char = []
    char.append(inp[0])
    l = 0
    for i in range(len(inp) - 1):
        r = i+1
        if len(char) == 14:
            print(char)
            return r
        if inp[r] in char:
            idx = next((i for i, v in enumerate(char) if v == inp[r]), None)
            del char[:idx+1]
            l += 1
        char.append(inp[r])
            

if __name__ == "__main__":
    res = get_diff_2(input)
    print(res)