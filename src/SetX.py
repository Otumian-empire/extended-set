class SetX(set):
    """ An extension of the set class with additional methods for set cardinality, cartesian product, power set, etc """

    def __init__(self, iterable=[]):
        super().__init__()
        self.iterable = set(iterable)

    def __repr__(self):
        return f"<{self.__class__.__name__.upper()!a}> {self.iterable}"
