#!/usr/bin/python3

import click

@click.command('rd')
@click.option('-r','--recursive', default=1, help='Recursively list files.' )
@click.option('-f','--format'   , default='pretty', help='The person to greet.')
@click.option('-v','--verbose'   , default=1, help='The person to greet.')
@click.argument('path')

def read( recursive, format, verbose ):
    """Radioactive Shell!! """
    for x in range(recursive):
        click.echo('Hello %s!' % recursive)

#if __name__ == '__main__':
#    hello()

