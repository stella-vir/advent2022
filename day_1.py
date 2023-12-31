import sys

inputs = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

'''
inputs_max -> 24000
top_3 -> 45000

inputs0_max -> 68442
top_3 -> 204837

'''
inputs = inputs.strip().split('\n')
inputs.append('')

# inputs0 = open("day_1.txt", "r")
# inputs = inputs0.read().strip().split("\n")

# print(inputs)



def get_sum(inp):
    sum = 0
    sum_array = []
    for i in range(len(inp)):
        if inputs[i] == '':
            sum_array.append(sum)
            sum = 0
        else:
            sum += int(inputs[i])
    return sum_array

def get_max(inp):
    max = 0
    sum_array = get_sum(inp)
    for i in range(len(sum_array)):
        max = sum_array[i] if sum_array[i] > max else max
    return max

def get_top_3(inp):
    top_3 = []
    sum_3 = 0
    sum_array = get_sum(inp)
    sum_array.sort()
    top_3 = sum_array[-1:-4:-1]
    for i in range(len(top_3)):
        sum_3 += top_3[i]
    return sum_3

if __name__ == "__main__":
    # res = get_max(inputs)
    res = get_top_3(inputs)
    
    print(res)

    


        