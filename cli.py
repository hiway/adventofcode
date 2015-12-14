import click


@click.group()
def cli():
    pass


@cli.group()
def day1():
    pass


@day1.command()
@click.argument('input_file', type=click.File())
def part1(input_file):
    from day1 import part1_stanta_floor_positioning_system
    for directions in input_file:
        floor = part1_stanta_floor_positioning_system(directions)
        print('Final Floor: {0}'.format(floor))


@day1.command()
@click.argument('input_file', type=click.File())
@click.option('--halt', type=int)
def part2(input_file, halt):
    from day1 import part2_santa_fps_halt
    for directions in input_file:
        position = part2_santa_fps_halt(directions, halt)
        if position is not None:
            print('Position: {0}'.format(position))
        else:
            print('Never reached floor: {0}'.format(halt))


@cli.group()
def day2():
    pass


@day2.command()
@click.argument('input_file', type=click.File())
def part1(input_file):
    from day2 import part1_wrapping_paper_estimate
    total = 0
    for dimensions in input_file:
        total += part1_wrapping_paper_estimate(dimensions)
    print('Total wrapping paper required: {0} sq ft'.format(total))
