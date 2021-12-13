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
            print(f"UH OH!!!\n{results[0]} results were not correct! We were expecting {self.answer}, but {results[1]} was the intended result of the function.")
    return wrapper


class Test():
    def __init__(self, x, y, answer):
        self.x = x
        self.y = y
        self.answer = answer
        self.b4()

    @print_decorator
    def b4(self):
        test = "Bomb Baby 4"
        result = bb4.solution(self.x, self.y)
        return test, result

    # @print_decorator
    # def b3(self):
    #     test = "Bomb Baby 3"
    #     result = bb3.solution(self.x, self.y)
    #     return test, result, self.name


def int_gen(): 
    return random.randint(1, 10**50)


test_1 = Test('2', '1', '1')
test_2 = Test('4', '7', '4')
test_3 = Test('2', '4', 'impossible')
test_4 = Test(int_gen(), int_gen(), 'test')

