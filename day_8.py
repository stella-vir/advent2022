inputs = '''
30373
25512
65332
33549
35390
'''

'''
16 outside + 5 inside
21
'''

inputs = inputs.strip().split('\n')

x_len = len(inputs[0])
y_len = len(inputs)
outside = 2 * (x_len - 2 + y_len)
print('outside', outside)

for x in range(1, x_len-1):
    for y in range(1, y_len-1):
        print('coord', x, y, inputs[x][y])