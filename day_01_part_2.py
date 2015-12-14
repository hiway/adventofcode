"""
http://adventofcode.com/day/1

--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?
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
@click.option('--halt_at_floor', type=int, default=None)
def santa_walk(directions, halt_at_floor):
    """
    Usage: python day_01_part_2.py --halt_at_floor=2 "()()((()(()())()("

    :param directions: string containing either ( or )
    :param halt_at_floor: integer, floor where we want to get position
    :return:
    """
    floor = 0
    position = 1
    for direction in directions:
        floor += change_floor(direction)
        if halt_at_floor == floor:
            print('Position: {0}'.format(position))
            break
        position += 1
    print('Final floor: {0}'.format(floor))


if __name__ == '__main__':
    santa_walk()
