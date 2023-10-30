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
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
-> CMZ

position
1 1
5 2 // 4 + 1
9 3 
13 4 

[D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
move 1 from 2 to 1
1 2 1


'''

input = input.split('\n')
# print(input)

def parse(inp):
    moves = []
    matrix = {}
    for line in inp:
        if line.startswith('move'):
            line = line.split(' ')
            amt, start, end = line[1], line[3], line[5]
            moves.append((amt, start, end))
        elif line != '':
            for i, char in enumerate(line):
                if char.isalpha():
                    matrix[char] = i
    return moves, matrix


def get_matrix(matrix):
    matrix = {k: v // 4 + 1 for k, v in matrix.items()}

    return matrix          

def get_top(matrix):
    bucket = {}
    ls = []
    for k, v in matrix.items():
        print(k, v)
        if v in bucket:
            print('ifffff')
            print(bucket[v])
            # bucket[v].append(k)
            bucket[v].insert(0, v)
        else:
            print('elseeee')
            bucket[v] = [k]
    # bucket = dict(sorted(bucket.items()))
    print(bucket)  
    return bucket


def get_bucket(matrix, start, end):
    bucket = get_top(matrix)
    for k, v in bucket.items():
        if k == start:
            matrix[k] = end
  
      


def get_moves(moves, matrix):
    for move in moves:
        amt, start, end = move
        amt = int(amt)
        start = int(start)
        end = int(end)
        for i in range(amt):
            get_bucket(matrix, start, end)
  

def get_slacks(inp):
    moves, matrix = parse(inp)
    matrix = get_matrix(matrix)
    print(matrix)
    get_moves(moves, matrix)



res = get_slacks(input)
#print(res)