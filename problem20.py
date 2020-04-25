'''

Define a class with a generator which can iterate the numbers, 
which are divisible by 7, between a given range 0 and n.

'''

class Gen_Num_7():
    def __init__(self, n):
        self.n = n
    def next_num(self):
        for num in range(self.n):
            if num*7<self.n:
                yield num*7

if __name__ == "__main__":

    number = Gen_Num_7(20)
    gen_num = number.next_num()
    print(gen_num.__next__())
    print(gen_num.__next__())
    print(gen_num.__next__())
