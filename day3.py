import collections


def get_next_coordinates(x, y, direction):
    """
    >>> get_next_coordinates(0, 0, '>')
    (1, 0)

    >>> get_next_coordinates(0, 0, '<')
    (-1, 0)

    >>> get_next_coordinates(0, 0, '^')
    (0, 1)

    >>> get_next_coordinates(0, 0, 'v')
    (0, -1)
    """
    if direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    elif direction == '<':
        x -= 1
    elif direction == '>':
        x += 1
    else:
        raise SyntaxError('Expected <^v> got {0}'.format(direction))
    return x, y


def part1_sanda_gps(directions):
    """
    --- Day 3: Perfectly Spherical Houses in a Vacuum ---

    Santa is delivering presents to an infinite
    two-dimensional grid of houses.

    He begins by delivering a present to the house at his
    starting location, and then an elf at the North Pole
    calls him via radio and tells him where to move next.
    Moves are always exactly one house to the north (^),
    south (v), east (>), or west (<). After each move,
    he delivers another present to the house at his new
    location.

    However, the elf back at the north pole has had a
    little too much eggnog, and so his directions are a
    little off, and Santa ends up visiting some houses
    more than once. How many houses receive at least
    one present?

    For example:
    > delivers presents to 2 houses: one at the starting
        location, and one to the east.

    >>> part1_sanda_gps('>')
    2

    ^>v< delivers presents to 4 houses in a square,
        including twice to the house at his starting/
        ending location.

    >>> part1_sanda_gps('^>v<')
    4

    ^v^v^v^v^v delivers a bunch of presents to some very
        lucky children at only 2 houses.

    >>> part1_sanda_gps('^v^v^v^v^v')
    2
    """
    visits = collections.Counter(['0_0'])
    x, y = 0, 0
    for direction in directions:
        x, y = get_next_coordinates(x, y, direction)
        pin = '{0}_{1}'.format(x, y)
        visits.update([pin])
    return sum([1 for val in visits.values() if val >= 1])


def part2_santa_and_robo_santa_gps(directions):
    """
    --- Part Two ---

    The next year, to speed up the process, Santa creates a
    robot version of himself, Robo-Santa, to deliver presents
    with him.

    Santa and Robo-Santa start at the same location (delivering
    two presents to the same starting house), then take turns
    moving based on instructions from the elf, who is eggnoggedly
    reading from the same script as the previous year.

    This year, how many houses receive at least one present?

    For example:

    ^v delivers presents to 3 houses, because Santa goes north,
        and then Robo-Santa goes south.

    >>> part2_santa_and_robo_santa_gps('^v')
    3

    ^>v< now delivers presents to 3 houses, and Santa and
        Robo-Santa end up back where they started.

    >>> part2_santa_and_robo_santa_gps('^>v<')
    3

    ^v^v^v^v^v now delivers presents to 11 houses, with Santa
        going one direction and Robo-Santa going the other.

    >>> part2_santa_and_robo_santa_gps('^v^v^v^v^v')
    11
    """
    import collections

    santa_visits = collections.Counter(['0_0'])
    robo_visits = collections.Counter()

    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    santa_turn = True

    for direction in directions:
        if santa_turn is True:
            santa_x, santa_y = get_next_coordinates(santa_x, santa_y, direction)
            pin = '{0}_{1}'.format(santa_x, santa_y)
            santa_visits.update([pin])
            santa_turn = False
        else:
            robo_x, robo_y = get_next_coordinates(robo_x, robo_y, direction)
            pin = '{0}_{1}'.format(robo_x, robo_y)
            robo_visits.update([pin])
            santa_turn = True

    final_map = santa_visits + robo_visits
    return sum([1 for val in final_map.values() if val >= 1])
