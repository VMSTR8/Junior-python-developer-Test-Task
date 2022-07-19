from typing import Union


def find_index_from_string(
        array: str,
        element_to_find: int
) -> Union[int, str]:
    try:
        return [int(number) for number in array].index(element_to_find)
    except ValueError:
        return f'{element_to_find} is not in list'


if __name__ == '__main__':
    print(find_index_from_string('1111111111110000000000000', 0))  # OUT: 12
