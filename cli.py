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
    from day1 import part1
    for directions in input_file:
        print('Final Floor: {0}'.format(part1(directions)))


@day1.command()
@click.argument('input_file', type=click.File())
@click.option('--halt', type=int)
def part2(input_file, halt):
    from day1 import part2
    for directions in input_file:
        position = part2(directions, halt)
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
