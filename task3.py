import itertools
from typing import Generator

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


def all_timestamps(massive: dict) -> Generator:
    for iteration in massive.values():
        yield from zip(iteration, itertools.cycle((-1, 1)))


def presence(massive: dict) -> Generator:
    counter_previous = 0
    for time, border in sorted(all_timestamps(massive)):
        counter_next = counter_previous + border
        if counter_previous == -2 and counter_next == -3:
            yield time, border
        if counter_previous == -3 and counter_next == -2:
            yield time, border
        counter_previous = counter_next


def appearance(massive: dict) -> int:
    return sum(time * border for time, border in presence(massive))


if __name__ == '__main__':
    appearance(tests[0]['data'])  # OUT: 3117
    appearance(tests[1]['data'])  # OUT: 3641
    appearance(tests[2]['data'])  # OUT: 3565
