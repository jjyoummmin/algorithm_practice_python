from functools import reduce

def to_124(n):
    str_124 = lambda x : ['1','2','4'][x]

    subtractor = 0
    divider = 1
    arr = []
    while n >= subtractor:
        digit = (n - subtractor) % ( divider * 3 ) // divider
        arr.append(str_124(digit))

        divider *= 3
        subtractor += divider
    
    # return ''.join(arr[::-1])
    return reduce(lambda a, x: x+a, arr)

for x in range(1, 20):
    print(x, to_124(x-1))

def solution(x):
    answer = to_124(x-1)
    return answer
