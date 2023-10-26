import sys

input0 = open("day_1.txt", "r")

input = '''
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

sum = 0
sum_array = []
max = 0
top_3 = []
sum_3 = 0



'''
input_max -> 24000
top_3 -> 45000

input0_max -> 68442
top_3 -> 204837

'''



# input = input.split("\n")
# input = input[1:-1]

input = input0.read().split("\n")
input.append('')
print(input[0])
print(input[-1])
print(len(input))


for i in range(len(input)):
    if input[i] == '':
       sum_array.append(sum)
       sum = 0
    else:
        sum += int(input[i])


for i in range(len(sum_array)):
    max = sum_array[i] if sum_array[i] > max else max


sum_array.sort()
# print(sum_array)
print(max)
top_3 = sum_array[-1:-4:-1]
print(top_3)
for i in range(len(top_3)):
    sum_3 += top_3[i]
print(sum_3)

    


        