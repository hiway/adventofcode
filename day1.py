def change_floor(direction):
    if direction == '(':
        return 1  # up one floor
    if direction == ')':
        return -1  # down one floor
    # We shouldn't reach this point under normal operation, however,
    # if we do, there is an error in the input and we cannot continue.
    raise SyntaxError('Expected ( or ) , got {0}'.format(direction))


def part1(directions):
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
    floor = 0
    # Go through each character and update floor
    for direction in directions:
        floor += change_floor(direction)

    return floor


def part2(directions, halt_on_floor):
    """
    http://adventofcode.com/day/1

    --- Part Two ---

    Now, given the same instructions, find the position of the
    first character that causes him to enter the basement
    (floor -1). The first character in the instructions has
    position 1, the second character has position 2, and so on.

    For example:

        ) causes him to enter the basement at character position 1.
        ()()) causes him to enter the basement at character position 5.

    What is the position of the character that causes Santa
    to first enter the basement?
    """
    floor = 0
    position = 0
    for direction in directions:
        position += 1
        floor += change_floor(direction)
        if halt_on_floor == floor:
            return position
    return None
