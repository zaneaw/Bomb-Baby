import bombbaby
import random

def print_decorator(func_to_dec):
    def wrapper(obj):
        results = func_to_dec(obj)
        print("\n\n\n==========================================================================\n")
        print(f"Preparing to run the {results[0]} simulation.\nWe are testing:")
        print(f"  Mach:  {obj.x}\nFacula:  {obj.y}\n")
        print(f"Booting up the test. Standby...\n")
        if obj.answer == results[1] or obj.answer == 'test':
            print("The results are back!\n")
            if results[1] != 'impossible':
                print(f"It will only be {results[1]} generation(s) until we can destroy the LAMBCHOP doomsday device!!!!")
            else: print("But... We are DOOMED! It is IMPOSSIBLE...")
        else:
            print(f"UH OH!!!\n{results[0]} results were not correct! We were expecting '{obj.answer}', but got '{results[1]}' as a result of the function.")
    return wrapper


class Test():
    def __init__(self, x, y, answer):
        self.x = x
        self.y = y
        self.answer = answer
        self.bb()

    @print_decorator
    def bb(self):
        test = "Bomb Baby"
        result = bombbaby.solution(self.x, self.y)
        return test, result


def int_gen(): 
    return random.randint(1, 10**50)

x = int_gen()

test1 = Test('2', '1', '1')
test2 = Test('4', '7', '4')
test3 = Test('2', '4', 'impossible')
test4 = Test('2591', '9152', '26')
# test5 = Test(x, x, 'test')

