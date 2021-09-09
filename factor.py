
import bisect
import math
import sys


class Phactor(object):

    def __init__(self, onumber, tried=set()):

        self.onumber = onumber
        self.sqrt = int(math.sqrt(self.onumber))
        self.half = self.onumber // 2
        self.tried = tried
        self.factors = set()
        self.todo = set()
        self.nexts = []

    def add(self, n):

        if n <= (self.sqrt + 2) and n not in self.tried and n not in self.todo:
            bisect.insort(self.nexts, n)
            self.todo.add(n)

    def get(self):

        n = self.nexts.pop()
        n = self.todo.pop()

        return n

    def factorlr(self):

        factors = set()
        self.add(self.sqrt)
        self.add(self.sqrt + 1)

        while self.todo:
            self.factorl(factors)

        return factors

    def factorl(self, factors):

        number = self.get()

        if number <= 2 \
                or number in self.tried:
            return ()

        self.tried.add(number)

        next_ = number // 2
        mod = number % 2
        onext = self.onumber // number
        omod = self.onumber % number

        if not omod:
            factors.add(self.onumber // onext)
            factors.add(onext)

        to_try = (
            lambda ne, nu, onu: (onu // nu),
            lambda ne, nu, onu: (onu // nu) + 1,
            lambda ne, nu, onu: (onu // (nu + 1)),
            lambda ne, nu, onu: (onu // (nu + 1)) + 1,
            lambda ne, nu, onu: (onu // ne),
            lambda ne, nu, onu: (onu // ne) + 1,
            lambda ne, nu, onu: (onu // (ne + 1)),
            lambda ne, nu, onu: (onu // (ne + 1)) + 1,
            lambda ne, nu, onu: ne,
            lambda ne, nu, onu: ne + 1,
            lambda ne, nu, onu: nu - (ne // 2),
            lambda ne, nu, onu: nu - (ne // 2) + 1,
            lambda ne, nu, onu: nu - (ne // 2) + 2,
            lambda ne, nu, onu: nu - (ne // 2) + 3,
            lambda ne, nu, onu: nu - ((ne + 0) // 3),
            lambda ne, nu, onu: nu - ((ne + 0) // 3) + 1,
            lambda ne, nu, onu: nu - ((ne + 0) // 3) + 2,
            lambda ne, nu, onu: nu - ((ne + 0) // 3) + 3,
            lambda ne, nu, onu: nu - ((ne + 0) // 3) + 4,
            lambda ne, nu, onu: nu - ((ne + 0) // 3) + 5,
            lambda ne, nu, onu: (ne // 2),
            lambda ne, nu, onu: (ne // 2) - 1,
            lambda ne, nu, onu: (ne // 2) - 2,
            lambda ne, nu, onu: (ne // 2) - 3,
            lambda ne, nu, onu: ((ne + 0) // 3),
            lambda ne, nu, onu: ((ne + 0) // 3) - 1,
            lambda ne, nu, onu: ((ne + 0) // 3) - 2,
            lambda ne, nu, onu: ((ne + 0) // 3) - 3,
            lambda ne, nu, onu: ((ne + 0) // 3) - 4,
            lambda ne, nu, onu: ((ne + 0) // 3) - 5,
        )

        for tt in to_try:
            n = tt(next_, number, self.onumber)
            self.add(n)

def main(number_string):

    number = int(number_string.replace(',', ''))

    print(f'factoring: {number}')

    p = Phactor(number)
    fs = p.factorlr()

    print(f'tries: {len(p.tried)}, max tried: {max(p.tried)}, factors: {tuple(sorted(fs))}')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))


