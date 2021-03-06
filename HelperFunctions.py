import itertools

def ilen(iterable):
    return sum(1 for _ in iterable)

def first(iterable, condition = lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    Raises `StopIteration` if no item satysfing the condition is found.

    >>> first( (1,2,3), condition=lambda x: x % 2 == 0)
    2
    >>> first(range(3, 100))
    3
    >>> first( () )
    Traceback (most recent call last):
    ...
    StopIteration
    """

    return next(x for x in iterable if condition(x))
    
def permutation(list1,list2):
    return list(set(map(' '.join, itertools.chain(itertools.product(list1, list2), itertools.product(list2, list1)))))