from functools import partial
from memory_profiler import profile
from itertools import chain

nums=range(1,2*10**4+1)

# using lambdas only:
fizzbuzz = lambda x: "fizzbuzz" if isinstance(x, int) and not x%15 and not isinstance(x, str) else x
fizz = lambda x: "fizz" if isinstance(x, int) and not x % 3 and not isinstance(x, str) else x
buzz = lambda x: "buzz" if isinstance(x, int) and not x % 5 and not isinstance(x, str) else x


def mapf(f_list, argument):
    """map multiple functions to a single argument without recursion""" 
    r = argument
    for f in f_list:
        r = map(f, r)

    return r

# with yield
def fizzbuzzfilter(test, num, word):
    if (type(test) != int) or (test%num):
        yield test
    else:
        yield word

filter3y = partial(fizzbuzzfilter, num=3, word='fizz')
filter5y = partial(fizzbuzzfilter, num=5, word='buzz')
filter15y = partial(fizzbuzzfilter, num=15, word='fizzbuzz')


def mapf_chain(f_list, argument):
    """apply a list of functions to a single argument, without recursion"""
    r = argument
    for f in f_list:
        #  r = chain(*(map(f, r)))  # same as below, but with uglier syntax
        r = chain.from_iterable(map(f, r))
        
    return r



# no yields

def fizzbuzzfilter(test,num, word):
    if (type(test) != int) or (test%num):
        return test
    else:
        return word

filter3 = partial(fizzbuzzfilter, num=3, word='fizz')
filter5 = partial(fizzbuzzfilter, num=5, word='buzz')
filter15 = partial(fizzbuzzfilter, num=15, word='fizzbuzz')

def map_many(iterable, function, *other):
    """map many functions to a single iterable"""
    if other:
        return map_many(map(function, iterable), *other)
    return map(function, iterable)

@profile
def lazy():
    """no recursion, with yield"""
    return list(mapf_chain([filter15y, filter3y, filter5y], nums))


@profile
def lumber():   
    """calling map f, no recursion, with lambdas"""
    return list(mapf([fizzbuzz, fizz, buzz], nums))


@profile
def no_y():
    """no yield, recursion"""
    return list(map_many(nums, filter15, filter3, filter5))

@profile
def chain():
    return list(filter5y(filter3y(filter15y(nums))))

#lazy()
#lumber()
#no_y()
chain()
