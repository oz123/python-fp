from functools import partial
from memory_profiler import profile

def fizzbuzzfilter(test, num, word):
    if (type(test) != int) or (test%num):
        yield test
    else:
        yield word

filter3 = partial(fizzbuzzfilter, num=3, word='fizz')
filter5 = partial(fizzbuzzfilter, num=5, word='buzz')
filter15 = partial(fizzbuzzfilter, num=15, word='fizzbuzz')

nums=range(1,20000001)

from itertools import chain
def mapf(f_list, argument):
    """apply a list of functions to a single argument, without recursion"""
    r = argument
    for f in f_list:
        #  r = chain(*(map(f, r)))  # same as below, but with uglier syntax
        r = chain.from_iterable(map(f, r))
        
    return r


@profile
def lazy():
    return list(mapf([filter15, filter3, filter5], nums))


