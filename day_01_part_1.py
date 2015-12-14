"""
http://adventofcode.com/day/1

Santa is trying to deliver presents in a large apartment building,
but he can't find the right floor - the directions he got are a
little confusing. He starts on the ground floor (floor 0) and then
follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a
closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep;
he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.
"""

import click


def change_floor(direction):
    if direction == '(':
        return 1  # up one floor
    if direction == ')':
        return -1  # down one floor
    # We shouldn't reach this point under normal operation, however,
    # if we do, there is an error in the input and we cannot continue.
    raise SyntaxError('Expected ( or ) , got {0}'.format(direction))


@click.command()
@click.argument('directions', type=str)
def santa_walk(directions):
    """
    Usage: python day_01_part_1.py "()()((()(()())()("

    :param directions: string containing either ( or )
    :return:
    """

    floor = 0
    for direction in directions:
        floor += change_floor(direction)
    print('Final floor: {0}'.format(floor))


if __name__ == '__main__':
    santa_walk()
