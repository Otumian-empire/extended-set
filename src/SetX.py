class setx:

    def __init__(self, size=0, iterable=[]):
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
                f"Can not pop from empyt {self.__class__.name.lower()}")
        self.iterable.pop()
        self.size -= 1

    def cardinality(self):
        return self.size

    def get(self):
        return self.iterable

    def new(self, size=0, iterable=[]):
        self.size = size
        self.iterable = set(iterable)

    def difference(self, other):
        if type(other) not in [list, set, dict]:
            raise TypeError(f"{self.__name__ !a} requires an iterable")
        return set([element for element in self.iterable if element in other])
