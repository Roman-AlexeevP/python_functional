from pymonad.operators.maybe import Just
from pymonad.tools import curry


@curry(2)
def add(x, y):
    return x + y


def add10(x):
    return add * Just(10) & x

