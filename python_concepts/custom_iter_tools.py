from typing import Iterable, Any, Callable, Union, List, Tuple, Dict, Set, Generator, Optional

def zip(*iterables: List[Iterable]) -> Generator:
    sentinel = object() #This will be used to catch when the __next__ on iterator object is exchausted. Next takes aditional param that returns upon exchaustion.

    iterators = [iter(iterable) for iterable in iterables] #convert all iterables to iterators, so the items are exhausted as we go over each iterator.
    while iterators: #servers as an infinite loop really, each time we will take the first element of each iterator, so next run all the iterables will have that element removed.
        group = []
        for iterator in iterators:
            next_item = next(iterator, sentinel)
            if next_item is sentinel:
                return
            group.append(next_item)

        yield tuple(group)

def enumerate(iterable: Iterable, start: int = 0) -> Generator:
    count = start
    i1 = iter(iterable)
    sentinel = object()
    while True:
        next_item = next(i1, sentinel)
        if next_item is sentinel:
            return
        
        yield (count, next_item)
        count += 1

def map(fn: callable, iterable: Iterable) -> Generator:
    i1 = iter(iterable)
    sentinel = object()
    while True:
        next_item = next(i1, sentinel)
        if next_item is sentinel:
            return

        yield fn(next_item)

xd = iter([1,2,3,4])
print(list(zip(xd, xd)))

for tup in enumerate([1,2,3]):
    print(tup)

print(list(map(len, ['abc', 'de', 'fghi'])))
