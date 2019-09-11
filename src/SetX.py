class setx:

    def __init__(self, iterable, size):
        self.size = size
        self.iterable = set(iterable)

    def __repr__(self):
        return f"<{self.__class__.__name__.lower()!a}> {self.iterable}"

    def add(self, element):
        self.iterable.add(element)
        self.size += 1

    def clear(self):
        self.iterable = set()
        self.size = 0

    def pop(self):
        if self.size < 1:
            raise KeyError(
                f"Can not pop from empyt {self.__name__.lower()}")
        self.iterable.pop()
        self.size -= 1

    def size(self):
        return self.size

    def get(self):
        return self.iterable

    def new(self, iterable, size):
        self.size = size
        self.iterable = set(iterable)

    def check_type(self, other):
        if type(other) not in [list, set, dict]:
            raise TypeError(f"{self.__name__ !a} requires an iterable")

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

        other = set(other)

        for element in self.iterable:
            if element not in other:
                return False
        return True

    def issuperset(self, other):
        self.check_type(other)

        other = set(other)

        for element in other:
            if element not in self.iterable:
                return False
        return True

    def remove(self, element):
        if element not in self.iterable:
            raise KeyError(f"{element!a} not found {self.get()}")

        temp = list(self.iterable)

        index = temp.index(element)

        del temp[index]

        self.iterable = set(temp)

        return index
