class setx:

    def __init__(self, iterable=[]):
        self.iterable = set(iterable)
        self.size = len(self.iterable)

    def __repr__(self):
        return f"<{self.__class__.__name__.lower() !a}> {self.iterable}"

    def add(self, element):
        if element not in self.iterable:
            self.iterable.add(element)
            self.size += 1
            print(element, self.iterable)

    def add_s(self, elements):
        temp = list(self.iterable)
        temp.extend(elements)
        self.iterable = set(temp)

        self.size = len(self.iterable)

    def clear(self):
        self.iterable = setx()
        self.size = 0

    def pop(self):
        if self.size < 1:
            raise KeyError(
                f"Can not pop from empyt {self.__name__.lower()}")
        self.iterable.pop()
        self.size -= 1

    def get_size(self):
        return self.size

    def get_elements(self):
        return self.iterable

    def new(self, iterable=[]):
        # self.iterable = setx(iterable)
        self.iterable = iterable
        s = setx(self.iterable)
        self.size = s.get_size()

    def check_type(self, other):
        if type(other) not in [list, set, dict, tuple, setx]:
            raise TypeError(
                f"{self.__class__.__name__ !a} requires an iterable")
        # else:
        #     return f"{type(other)!a}"

    def difference(self, other):
        self.check_type(other)

        difference = set()
        other = set(other)

        for element in self.iterable:
            if element not in other:
                difference.add(element)

        return difference

    def intersection(self, other):
        self.check_type(other)

        intersection = set()
        other = set(other)

        for element in self.iterable:
            if element in other:
                intersection.add(element)

        return intersection

    def isdisjoint(self, other):
        self.check_type(other)

        other = set(other)

        if not self.intersection(other):
            return True
        return False

    def issubset(self, other):
        self.check_type(other)

        other = list(set(other))
        size_of_others = 0

        for element in other:
            if element in self.iterable:
                size_of_others += 1

        if size_of_others == len(other):
            return True
        return False

    def issuperset(self, other):
        self.check_type(other)
        other = set(other)

        for element in self.iterable:
            if element not in other:
                return False
        return True

    def remove(self, element):
        if element not in self.iterable:
            raise KeyError(f"{element!a} not found {self.get()}")

        temp = list(self.iterable)

        index = temp.index(element)

        del temp[index]

        self.iterable = set(temp)
        self.size = len(self.iterable)

        return index

    def symmetric_difference(self, other):
        self.check_type(other)
        other = set(other)

        intersection = self.intersection(other)
        symmetric_difference = set()

        new_set = list(self.iterable) + list(other)
        new_set = set(new_set)

        for element in new_set:
            if element not in intersection:
                symmetric_difference.add(element)

        return symmetric_difference

    def cartesian_product(self, other):
        # A x B = {(a, b)| a in A, b in B}
        # |A x B| = |A| x |B| for A, B which are finite

        self.check_type(other)
        other = set(other)

        size_cartesian_product = self.get_size() * len(other)

        cartesian_product = set()

        for a in self.iterable:
            for b in other:
                cartesian_product.add((a, b))

        return cartesian_product, size_cartesian_product

    def power_set(self):
        pass
        # Let A be a finite set, n = |A | and P(A) be the power set of A
        # P(A) = {X: X is a subset of A}, | P(A) | = 2 ** |A | = 2 ** n
        #
        # From the above there'd be n inserts
        # P(A) may have {{}, {{X}: X in A}, ..., {{x1, x2, x3, ..., xn}: x in A}}
        # then we'd fill up the ' ... '
        #
        # if n > 2
        # there is no repetition as such {x1, x2} is the same as {x2, x1} and so on
        # we could make use of 3 sets, A, tempA and tempB (where tempA and tempB
        # are temporary variables)
        # have two loops
        # 1 - loop(0, n - 2)
        # 2 - loop(0, n - 1)
        # take from tempA, add from A to from tempB
        # add tempB to the power set and make tempA tempB
