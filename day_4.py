inputs = '''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''


'''
2-8 > 3-7
l1 l2 r1 r2
6-6 < 4-6
2

overlap
5-7,7-9 -> 7
2-8,3-7 -> 3-7
6-6,4-6 -> 6
2-6,4-8 -> 4-6
4

a b c d
a < c -> not overlap -> b < c
a > c -> not overlap -> d < a

'''

inputs = inputs.strip().split('\n')

# inputs0 = open('day_4.txt', 'r').read()
# inputs = inputs0.strip().split('\n')

# print(inputs)



def get_edges(inp):
    edges = []
    for item in inp:
        l, r= item.split(',')
        l1, l2 = l.split('-')
        r1, r2 = r.split('-')
        edges.append((int(l1), int(l2), int(r1), int(r2)))

    return edges
   

def get_comprison(a, b, c, d):
    if (a > c and b > d) or (a < c and b < d):
        return 0
    else:
        return 1


def get_ctn(inp):
    count = 0
    edges = get_edges(inp)
    for item in edges:
        l1, l2, r1, r2 = item[0], item[1], item[2], item[3]
        res = get_comprison(l1, l2, r1, r2)
        if res == 1:
            count += 1
    return count

def get_overlap(a, b, c, d):
    if a == c:
        return 1
    elif a < c:
        if b < c:
            return 0
        else:
            return 1
    else:
        if d < a:
            return 0
        else:
            return 1

def get_ctn_2(inp):
    count = 0
    edges = get_edges(inp)
    for item in edges:
        l1, l2, r1, r2 = item[0], item[1], item[2], item[3]
        res = get_overlap(l1, l2, r1, r2)
        if res == 1:
            count += 1
    return count

if __name__ == "__main__":
    # res = get_ctn(inputs)
    res = get_ctn_2(inputs)
    
    print(res)



