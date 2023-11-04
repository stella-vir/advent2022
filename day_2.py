import sys

inputs = '''
A Y
B X
C Z
'''

inputs = inputs.strip().split('\n')

# inputs0 = open('day_2.txt', 'r').read()
# inputs = inputs0.strip().split('\n')

# print(inputs)

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

def get_result(inputs):
    sum = 0
    for i in inputs:
        a, b = i.split(' ')
        sum += get_score(b)
        res = get_winner(a, b)
        if res == 'WIN':
            sum += 6
        elif res == 'DRAW':
            sum += 3

        print(sum)
    return sum

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

def get_result_2(inputs):
    sum = 0
    for i in inputs:
        a, b = i.split(' ')
        outcome = get_outcome(b)
        score, letter = get_letter(a, outcome)
        score2 = get_score(letter)
        sum += score + score2

    return sum

if __name__ == "__main__":
    # res = get_result(inputs)
    res = get_result_2(inputs)
    
    print(res)