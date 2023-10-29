import sys

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

# print(input)

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

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
-> r

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
-> Z

r 18 + Z 52  = 70

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



def get_sum(inp):
    sum = 0
    for i in inp:
        first, second = get_half(i)
        com = get_common_letter(first, second)
        sum += get_score(com)
    return sum

# res = get_sum(input)
# print(res)


def every_three_lines(inp):
    res = []
    for i in range(0, len(inp), 3):
        res.append([inp[i], inp[i+1], inp[i+2]])
    return res

def find_common(a, b, c):
    count_a = {}
    count_b = {}
    count_c = {}

    # count the occurence of the letters
    for item in a:
        count_a[item] = count_a.get(item, 0) + 1

    for item in b:
        count_b[item] = count_b.get(item, 0) + 1
    
    for item in c:
        count_c[item] = count_c.get(item, 0) + 1

    for item, count in count_a.items():
        if item in count_b and item in count_c:
            return item


def get_sum_2(inp):
    sum = 0
    arr = every_three_lines(inp)
    for item in arr:
        first, second, third = item[0], item[1], item[2]
        com = find_common(first, second, third)
        sum += get_score(com)
    return sum

res = get_sum_2(input)
print(res)

