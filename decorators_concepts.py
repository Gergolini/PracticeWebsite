import time

def func_add1(number):
    return number + 1

def func_add1_nested(number):

    def adding(number):
        return number + 1

    return adding(number)

def func_add1_nested_2(number):

    def adding():
        return number + 1

    return adding()

def func_add1_nested_3(number):

    def adding():
        return number + 1

    return adding

def nested_hi():
    def print_hi():
        return "Hi"
    return print_hi

def uppercase_decorator(function):
    def function_wrapper(*args):
        return function(*args).upper()
    return function_wrapper

def print_hello_word():
    return "hello world"

print(func_add1(5))
print(func_add1_nested(5))
print(func_add1_nested_2(5))
print(func_add1_nested_3(5)())
print(nested_hi()())

dec = uppercase_decorator(print_hello_word)
print(dec())

@uppercase_decorator
def say_qi():
    return "qi"

print(say_qi())

@uppercase_decorator
def say_gergo(gergo):
    return gergo

print(say_gergo("gergo"))

def timer(func):
    def function_wrapper(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        end = time.time()
        print("Function {} finished execution in {} millisecs.".format(func.__name__, (end-start)*1000))
    return function_wrapper


def add_bunch(*args):
    return sum(args)

print(add_bunch(2,3))
print(add_bunch(2,3,4))

def add_bunch_2(**kargs):
    for k, v in kargs.items():
        print("{}: {}".format(k, v))
    return sum(kargs.values())

print(add_bunch_2(a=2,b=3))
print(add_bunch_2(a=2,b=3,c=4))

def add_bunch_3(*args, **kargs):
    return sum(args) + sum(kargs.values())

print(add_bunch_3(8, 9, a=2,b=3, c=4))

def fib_recur(n):
    if n==0 or n==1: return 1
    return fib_recur(n-1) + fib_recur(n-2)

@timer
def fib_dp(n):
    if n==0 or n==1: return 1
    p = 1
    pp = 1
    for i in range(2,n+1):
        c = p + pp
        pp = p
        p = c
    print(c)

@timer
def _calc_fib(n):
    print(fib_recur(n))

_calc_fib(10)
fib_dp(10)
_calc_fib(30)
fib_dp(30)
