# Extended Set
This is an extension of the set class with additional methods for set cardinality, cartesian product, power set, etc. As an extension for the set class it is meant to work fine as a set.

# Classes
1. SetX

# Sources
1. [Python Documentation](https://python-3.7.3-docs-html/library/stdtypes.html#set-types-set-frozenset)
1. Book of Proof by Richard Hammack, chapter on sets - mathematical structures

# Operations on Set
1. `len(Set)`
1. _element_ `in` `Set`
1. _x_ `not` `in` `Set`
1. `isdisjoint`
1. `issubset`
1. `issuperset`
1. `union`
1. `difference`
1. `symmetric_difference`
1. `copy`
1. `add`
1. `remove`
1. `pop`
1. `discard`
1. `clear`
1. `intersection`

# Operations on SetX
1. `cardinality`
1. `isempty`
1. `cartesian_product`
1. `power_set`
1. `complement`
1. `iselement`

# Definitions of terms & operations on SetX
1. **`Cardinality`** : This is the size (magnitude) of a set. It is the number of elements in the set. <br>
    ```
    Eg: Given a set A = {1,2,3,4,5}, set A has a cardility of 5. This because the number of elements in set A is 5.
    ```

1. **`Empty(Null) Set`** : This is a set of size _zero_. This set has no elements. <br>
    ```
    Eg: Given a set E = {}, set E is an empty set or a null set.
    ```

1. **`Non-empty(null) sets`** : This is a set that has at least 1 element. This set is not empty or null.

1. **`Cartesian product`** : Given the sets, A and B as `non-empty` sets , denoted by `(A x B)` and defined as `(A x B) = {(a, b): a in A, b in B}`. <br>
    ```
    Eg: Given that set A = {1, 2, 3} and set B = {a, b}
    The cartesian product of A and B, (A x B) = {(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)}
    ```

1. **`Power set`** : Given a `non-empty` set A, the `power set` of A, which is another set, denoted by `P(A)` and defined to be the set of all subsets of A.
    ```
    Eg: Given set A = {1,2,3}
    The Power set of A, P(A) = {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
    ```

# Know that
1. The sweet terms are all from Mr. Richard Hammack
1. I will use informal language to express certain points
1. `cardinality` is the same as `len`(`set`)
1. `isempty` checks if `{}`
1. `complement`, `intersection`, `difference` and `disjoint` has something to do with each other.
