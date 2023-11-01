import sys

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


# input = input.split('\n')
input = open('day_5.txt').read().split('\n')
# print(input)

def parse(inp):
    matrix = {}
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
                    # duplicate letters
                    matrix[(stack, level+1)] = (char)
    return moves, matrix

def get_bucket(start, end, matrix, i):
    another_matrix = {}
    values_dict = {}

    for k, v in matrix.items():
        k0 = k[0]
        if k0 not in values_dict:
            values_dict[k0] = []
        values_dict[k0].append((k, v))
    print('values_dict', values_dict)
    sys.exit()

    for k, v in matrix.items():
        k0 = k[0]
        k1 = k[1]
        if k0 == start:
            print('moving pieces from ', (start, k1))
            if k1 == 1:
                another_matrix[(end, 1)] = v
            else:
                another_matrix[(start, k1 - 1)] = v
            if k0 == 2 and k1 == 3:
                print('another3', another_matrix)
            if k0 == 2 and k1 == 4:
                print('another4', another_matrix)
                sys.exit()
        if k0 == end:
            print('moving pieces to ', (end, k1))
            another_matrix[(end, k1 + 1)] = v
        else:
            another_matrix[k] = v

    matrix = another_matrix
    return matrix

def get_sequence(matrix):
    matrix = dict(sorted(matrix.items(), key=lambda item: item[0][0]))
    values_dict = {}
    val = {}
    new_matrix = {}

    # values_dict
    # {1: [((1, 1), 'M'), ((1, 2), 'F'), ((1, 3), 'C'), ((1, 4), 'W'), ((1, 5), 'T'), ((1, 6), 'D'), ((1, 7), 'L'), ((1, 8), 'B')], 2: [((2, 6), 'L'), ((2, 7), 'B'), ((2, 8), 'N')]}
    for k, v in matrix.items():
        k0 = k[0]
        if k0 not in values_dict:
            values_dict[k0] = []
        values_dict[k0].append((k, v))

    for key, values in values_dict.items():
        if key not in val:
            val[key] = 0
        for i, (k, v) in enumerate(values):
            if i == 0:
                if k[1] != 1:
                    k = (k[0], 1)
            else:
                val[key] += 1
                k = (k[0], val[key]+1)
            new_matrix[k] = v
    matrix = new_matrix
    return matrix

def get_moves(moves, matrix):
    for move in moves:
        amt, start, end = move
        amt = int(amt)
        start = int(start)
        end = int(end)
        for i in range(amt):
            print('the ', i+1, ' round moving from', start, 'to ',  end)
            matrix = get_sequence(matrix)
            matrix = get_bucket(start, end, matrix, i)
        matrix = dict(sorted(matrix.items(), key=lambda item: item[0][0]))
        if start == 2:
            print(matrix)
            sys.exit()
    return matrix

def get_letters(matrix):
    matrix = dict(sorted(matrix.items(), key=lambda item: item[1][0]))
    letters = ''
    for k, v in matrix.items():
        if k[1] == 1:
            letters += v
    return letters

def get_crates(inp):
    moves, matrix = parse(inp)
    matrix = get_moves(moves, matrix)
    letters = get_letters(matrix)

    return letters

res = get_crates(input)
print(res)