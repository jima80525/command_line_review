#!/usr/bin/env python
import click


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-l', '--limit', type=int, default=0, help='Smallest value shown')
@click.option('-i', '--include', help='Show only these comma separated commands')
@click.option('-e', '--exclude', help='Exclude these comma separated commands')
@click.argument('logfiles', type=click.File('r'), nargs=-1)
def main(limit, include, exclude, logfiles):
    click.echo('limit = {0}'.format(limit))
    if include:
        click.echo('include passed: {0}'.format(include))
    if exclude:
        click.echo('exclude passed: {0}'.format(exclude))
    for f in logfiles:
        line = f.readline().strip()
        click.echo(line)


def fred():
    main(1, 'fred,wilma', 'jima, venitha', ['a', 'b', 'c'])

if __name__ == '__main__':
    # main()
    fred()
