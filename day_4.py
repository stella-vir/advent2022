input = '''
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
'''

input0 = open('day_4.txt', 'r').read()

# input = input.strip().split('\n')
input = input0.strip().split('\n')

# print(input)



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


res = get_ctn(input)
print(res)


