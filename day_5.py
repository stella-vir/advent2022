import sys
from collections import defaultdict

input = '''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

'''
i 0 1
1 2
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
-> CMZ

1 1
5 2 // 4 + 1
9 3 

{'N': (1, 2), 'Z': (1, 3), 'D': (2, 1), 'C': (2, 2), 'M': (2, 3), 'P': (3, 3)}
2 -> 1
'D': (2, 1) -> (1, 1)
'C': (2, 2) -> (2, 1)
'M': (2, 3) -> (2, 2)
'N': (1, 2) -> (1, 3)
'Z': (1, 3) -> (1, 2)

'''


input = input.split('\n')

def parse(inp):
    matrix = defaultdict(list)
    moves = []
    stack = 1
    for level, line in enumerate(inp):
        if line.startswith('move'):
            line = line.split(' ')
            amt, start, end = line[1], line[3], line[5]
            moves.append((amt, start, end))
        elif line != '':
            for i, char in enumerate(line):
                if char.isalpha():
                    stack = i // 4 + 1
                    matrix[char] = (stack, level)
    return moves, matrix

def get_bucket(start, end, matrix):
    print(start, '->', end)
    print('matrix', matrix)
    for k, v in matrix.items():
        if v[0] == start:
            if v[1] == 1:
                matrix[k] = (end, v[1])
                break
            else:
                print('k, v[1]', k, v[1])
                matrix[k] = (start, v[1] - 1)
                break
    print('matrix', matrix)
    sys.exit()

def get_moves(moves, matrix):
    matrix = dict(sorted(matrix.items(), key=lambda item: item[1][0]))
    not_one = defaultdict(list)
    prev = 0
    for i, (k, v) in enumerate(matrix.items()):
        if v[1] == 1:
            v0 = v[0]
            one = [(k, v) for k, v in matrix.items() if v[0] == v0]
            not_one = {k: {'value': v} for k, v in matrix.items() if k not in one[0]}
    print('not one', not_one)
    for i, (k, v) in enumerate(not_one.items()):
        print('k, v', k, v)
        if v['value'][0] != prev:
            v['value'] = (v['value'][0], 1)
        else:
            v['value'] = (v['value'][0], 2)
    prev = v['value'][0]
    print('not one', not_one)
    print(matrix)
    sys.exit()
    for move in moves:
        amt, start, end = move
        amt = int(amt)
        start = int(start)
        end = int(end)
        for i in range(amt):
            print('amt', amt, i)
            get_bucket(start, end, matrix)

def get_crates(inp):
    moves, matrix = parse(inp)
    get_moves(moves, matrix)

res = get_crates(input)
print(res)