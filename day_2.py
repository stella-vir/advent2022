import sys

input = '''
A Y
B X
C Z
'''

# input = input.strip().split('\n')

input0 = open('day_2.txt', 'r').read()
input = input0.strip().split('\n')

print(input)

'''
A Rock X
B Paper Y
C Scissors Z
PaperY 2 + Won 6
Rock 1 + Loss 0
Scissors 3 + Draw 3
Total 8 + 1 + 6 = 15

draw - lose - win
Y - X - Z
X - X - X
3 - 0 - 6
1 - 1 - 1
=12

'''

def get_winner(a, b):
    layer_1 = ['A', 'X']
    layer_2 = ['B', 'Y']
    layer_3 = ['C', 'Z']
    layers = [layer_1, layer_2, layer_3]

    for i, layer in enumerate(layers):
        if a in layers[i]:
            if b in layers[i]:
                return 'DRAW'
            elif b in layers[(i+1) % len(layers)]:
                return 'WIN'
            else:
                return 'LOSS'
    return 'Not Valid'
    


def get_score(a):
    if a == 'X':
        return 1
    elif a == 'Y':
        return 2
    elif a == 'Z':
        return 3
    return 0


def get_result(input):
    sum = 0
    for i in input:
        a, b = i.split(' ')
        print(a, b)
        sum += get_score(b)
        print(sum)
        res = get_winner(a, b)
        print(res)
        if res == 'WIN':
            sum += 6
        elif res == 'DRAW':
            sum += 3

        print(sum)
    return sum

# res = get_result(input)
# print(res)


def get_outcome(a):
    if a == 'X':
        return 'LOSE'
    elif a == 'Y':
        return 'DRAW'
    elif a == 'Z':
        return 'WIN'
    return 0

def get_letter(a, b):
    layer_1 = ['A', 'X']
    layer_2 = ['B', 'Y']
    layer_3 = ['C', 'Z']
    layers = [layer_1, layer_2, layer_3]

    for i, layer in enumerate(layers):
        if a in layers[i]:
            if b == 'WIN':
                return 6, layers[(i+1) % len(layers)][1]
            elif b == 'DRAW':
                return 3, layers[i][1]
            elif b == 'LOSE':
                return 0, layers[(i-1) % len(layers)][1]
    return 0, 'Not Valid'


def get_result_2(input):
    sum = 0
    for i in input:
        a, b = i.split(' ')
        print(a, b)
        outcome = get_outcome(b)
        score, letter = get_letter(a, outcome)
        score2 = get_score(letter)
        sum += score + score2

    return sum

res = get_result_2(input)
print(res)