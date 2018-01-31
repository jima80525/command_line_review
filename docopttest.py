#!/usr/bin/env python
'''
Usage:
    docopttest.py [options] [<logfiles>...]
    docopttest.py (-h | --help)

Options:
  -l, --limit=<int>          Smallest value shown
  -i, --include=<cmd,...>    Show only these comma separated commands
  -e, --exclude=<cmd,...>    Show only these comma separated commands
  -h, --help                 Show this message and exit.
'''
import docopt

def main(args):
    print('limit = {0}'.format(args['--limit']))
    if args['--include']:
        print('include passed: {0}'.format(args['--include']))
    if args['--exclude']:
        print('exclude passed: {0}'.format(args['--exclude']))
    for filename in args['<logfiles>']:
        with open(filename) as f:
            line = f.readline().strip()
            print(line)


if __name__ == '__main__':
    arguments = docopt.docopt(__doc__)
    main(arguments)
