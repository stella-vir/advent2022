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

# input = input.split('\n')
input = open('day_5.txt').read().split('\n')

def parse(inp):
    matrix = defaultdict(list)
    moves = []
    stack = 1
    for line in inp:
        if line.startswith('move'):
            line = line.split(' ')
            amt, start, end = line[1], line[3], line[5]
            moves.append((amt, start, end))
        elif line != '':
            for i, char in enumerate(line):
                if char.isalpha():
                    stack = i // 4 + 1
                    matrix[stack].append(char)
    return moves, matrix

def get_moves(moves, matrix):
    for move in moves:
        amt, start, end = move
        amt, start, end = int(amt), int(start), int(end)
        for i in range(amt):
            piece = matrix[start].pop(0)
            matrix[end].insert(0, piece)
    return matrix

def get_letters(matrix):
    first_letters = []
    letters = ''
    matrix = sorted(matrix.items(), key=lambda x: x[0])
    for k, v in matrix:
        if v:
            first_letters.append(v[0])

    letters = ''.join(first_letters)
    return letters

def get_bucket(inp):
    moves, matrix = parse(inp)
    matrix = get_moves(moves, matrix)
    letters = get_letters(matrix)
    return letters


# res = get_bucket(input)
# print(res)

def get_moves_2(moves, matrix):
    for move in moves:
        amt, start, end = move
        amt, start, end = int(amt), int(start), int(end)
        piece = matrix[start][0:amt]
        matrix[start] = matrix[start][amt:]
        matrix[end] = piece + matrix[end]
    return matrix

def get_bucket_2(inp):
    moves, matrix = parse(inp)
    matrix = get_moves_2(moves, matrix)
    letters = get_letters(matrix)
    return letters

res = get_bucket_2(input)
print(res)
