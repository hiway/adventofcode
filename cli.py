import click
import collections


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


@day2.command()
@click.argument('input_file', type=click.File())
def part2(input_file):
    from day2 import part2_ribbon_estimate
    total = 0
    for dimensions in input_file:
        total += part2_ribbon_estimate(dimensions)
    print('Total ribbon required: {0} ft'.format(total))


@cli.group()
def day3():
    pass


@day3.command()
@click.argument('input_file', type=click.File())
def part1(input_file):
    from day3 import part1_santa_gps
    for directions in input_file:
        print(part1_santa_gps(directions.strip()))


@day3.command()
@click.argument('input_file', type=click.File())
def part2(input_file):
    from day3 import part2_santa_and_robo_gps
    for directions in input_file:
        print(part2_santa_and_robo_gps(directions.strip()))


@cli.group()
def day4():
    pass


@day4.command()
@click.argument('secret_key')
def part1(secret_key):
    from day4 import part1_adventcoin_miner
    print(part1_adventcoin_miner(secret_key.strip()))


@day4.command()
@click.argument('secret_key')
@click.argument('match', default='000000')
def part2(secret_key, match):
    from day4 import part2_adventcoin_miner
    print(part2_adventcoin_miner(secret_key.strip(), match))


@cli.group()
def day5():
    pass


@day5.command()
@click.argument('input_file', type=click.File())
def part1(input_file):
    from day5 import part1_is_nice_string
    results = collections.Counter()
    results.update([part1_is_nice_string(directions.strip()) for directions in input_file])
    print(results.most_common(10))

