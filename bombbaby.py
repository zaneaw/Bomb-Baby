
##############################################################################
####################### Google Foobar Coding Challenge #######################
##############################################################################

def solution(x, y):
    # Track number of cycles starting from -1 to account for the
    # extra cycle added
    cycles = -1
    i = "impossible"
    nums_list = []

    # Convert string inputs to ints
    # Return if not possible
    try:
        x = int(x)
        y = int(y)
    except:
        return f"{i}, couldn't convert inputs to integers. Try again."

    # Create tuple out of the 2 arguments
    # Reassign them if need be
    values = x, y
    x, y = min(values), max(values)

    # Testing for simple inputs
    if x == 1 and y == 1:
        return "0"
    elif x <= 0 or y <= 0 or x == y: 
        return i
    else:
        '''No simple input detected, continue to try solving problem.
        Divide x by y and save that in p1.
        Modulo x by y and save that in p2.
        If p2 equals 0 and x doesn't equal 1, impossible.
        Check for end, otherwise tick cycles and
        convert y to now equal x and x is now equal to p2 and
        continue the cycle until x equals 0'''
        while x != 0:
            p1 = int(y / x) # EX. 14 / 3 = 4.667: p1 = 4
            p2 = int(y % x) # EX. 14 % 3 = 2:     p2 = 2
            if p2 == 0 and x != 1:
                return i
            # nums_list.insert(0, y)
            cycles += p1
            y = x
            x = p2
            if x == 0 and y == 1:
                return str(cycles)  #, nums_list


if __name__ == "__main__":
    # m1, f1 = '2', '1'
    # print(solution(m1, f1))

    # m2, f2 = '4', '7'
    # print(solution(m2, f2))

    # print(solution(5, 7))
    # print(solution(6, 1))
    # print(solution(2591, 9152))
    print(solution(25, 961))