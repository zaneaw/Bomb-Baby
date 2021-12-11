import random


def solution(x, y):
    cycles = 0
    i = "impossible"

    try:
        x = int(x)
        y = int(y)
    except:
        return i

    values = x, y
    x, y = min(values), max(values)
    if x == 1 and y == 1:
        return "0"
    if x <= 0 or y <= 0: 
        return i
    if x == y:
        return i
    else:
        while x != 0:
            p1 = int(y / x)
            p2 = int(y % x)
            if p2 == 0 and x != 1:
                return i
            cycles += p1
            if p2 == 0 and x == 1:
                return str(cycles - 1)
            y = x
            x = p2
        return str(cycles)


if __name__ == "__main__":
    # m1, f1 = '2', '1'
    # print(solution(m1, f1))

    # m2, f2 = '4', '7'
    # print(solution(m2, f2))

    m = random.randint(1, 10**50)
    f = random.randint(1, 10**50)
    print("Number 1:", m)
    print("Number 2:", f)
    print(solution(m, f))
    print(solution(5, 7))
    print(solution(6, 1))
    print(solution(2591, 9152))
