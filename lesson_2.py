from pymonad.tools import curry


@curry(2)
def str_conc(begin: str, end: str) -> str:
    return begin + end


hello_func = str_conc("Hello, ")


@curry(4)
def complex_greeting(greeting_word, greeting_delimiter, ending, name):
    return f"{greeting_word}{greeting_delimiter}{name}{ending}"


def configure_greeting(greeting_word, greeting_delimiter, ending):
    greeting_without_name = complex_greeting(greeting_word, greeting_delimiter, ending)
    return greeting_without_name
