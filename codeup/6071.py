# 0 이 입력될때까지 무한 출력
# 제너레이터로 구현해보자.

def stdin_generator():
    while True:
        yield int(input())


def print_until_zero():
    arr = stdin_generator()

    for x in arr:
        if (x==0): return
        print(x)

print_until_zero()