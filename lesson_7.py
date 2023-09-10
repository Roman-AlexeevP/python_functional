from pymonad import List

next_day = lambda pos: List(
        (pos[0], pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1]),
        (pos[0], pos[1] - 1)
)


def conquest_campaign(n: int, m: int, batalion: list, days_count: int = 1) -> int:
    if days_count == 1:
        batalion = List(*zip(*[iter(batalion)] * 2))

    is_valid = lambda pos: List(pos) if 1 <= pos[0] <= n and 1 <= pos[1] <= m else List()
    if len(batalion) == n * m:
        print(days_count)
    else:
        batalion = batalion >> next_day >> is_valid
        batalion = List(*set(batalion))
        days_count = days_count + 1
        conquest_campaign(n, m, batalion, days_count)


if __name__ == '__main__':
    conquest_campaign(3, 4, [2, 2, 3, 4])
