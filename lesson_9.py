from functools import reduce


lst = [15,1,25,2,30,3,10,5]


def create_pairs(iterable, prev_pair=None, all_pairs=None):
    if all_pairs is None:
        all_pairs = []
    if prev_pair is None:
        prev_pair = []
    if len(iterable) < 1:
        return all_pairs
    prev_pair.append(iterable.pop(0))
    if len(prev_pair) == 2:
        all_pairs.append(prev_pair)
        prev_pair = []
    return create_pairs(iterable, prev_pair, all_pairs)

def calculate_km(prev_state, curr_state):
    prev_km, prev_hours = prev_state
    curr_speed, curr_hours = curr_state
    return (prev_km + curr_speed *(curr_hours - prev_hours)), curr_hours


def odometer(oksana: list):
    time_with_speed_pairs = create_pairs(oksana)
    km, hours = reduce(
            calculate_km,
            time_with_speed_pairs,
            (0, 0)
    )
    return km

if __name__ == '__main__':
    print(odometer(lst)) # 90