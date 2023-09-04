from pymonad.Maybe import *

# посадка птиц на левую сторону
to_left = lambda num: lambda pos: (
    Nothing
    if abs((pos[0] + num) - pos[1]) > 4
    else Just((pos[0] + num, pos[1]))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda pos: (
    Nothing
    if abs((pos[1] + num) - pos[0]) > 4
    else Just((pos[0], pos[1] + num))
)

# банановая кожура
banana = lambda x: Nothing

# отображение результата
def show(maybe):
    if maybe == Nothing:
        print("failed")
    else:
        left, right = maybe.getValue()
        return Just((left, right))

# начальное состояние
begin = lambda: Just( (0,0) )


