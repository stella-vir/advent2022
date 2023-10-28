input = '''
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

'''

input0 = open('day_3.txt', 'r').read()

# input = input.strip().split('\n')
input = input0.strip().split('\n')

print(input)

'''
vJrwpWtwJgWr - hcsFMMfFFhFp -> p
jqHRNqRjqzjGDLGL - rsFMfFZSrLrFZsSL -> L
PmmdzqPrV - vPwwTWBwg -> P
v
t
s
a-z 1-26
A-Z 27-52
16+38+42+22+20+19 = 157
'''

def get_half(text):
    first = text[:len(text)//2]
    second = text[len(text)//2:]
    return [first, second]

def get_common_letter(a, b):
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if a[i] == b[j]:
    #             return a[i]

    index_a = {}

    for i, item in enumerate(a):
        index_a[item] = i

    for item in b:
        if item in index_a:
            return item

def get_score(letter):
    score = 0
    if letter.islower():
        score = ord(letter) - ord('a') + 1
    elif letter.isupper():
        score = ord(letter) - ord('A') + 27
    else:
        score = 0

    return score



def get_sum():
    sum = 0
    for i in input:
        first, second = get_half(i)
        com = get_common_letter(first, second)
        sum += get_score(com)
    return sum

# res = get_sum()
# print(res)


