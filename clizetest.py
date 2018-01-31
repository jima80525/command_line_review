#!/usr/bin/env python
import clize


def main(*input:clize.Parameter.REQUIRED, limit:'l'=0, include:'i'='',
         exclude:'e'=''):
    '''
    process log files

    :param input: log files to process
    :param include: Show only these comma separated commands
    :param exclude: Exclude these comma separated commands
    :param limit: Smallest value shown
    '''
    print('limit = {0}'.format(limit))
    if include:
        print('include passed: {0}'.format(include))
    if exclude:
        print('exclude passed: {0}'.format(exclude))
    for filename in input:
        with open(filename) as f:
            line = f.readline().strip()
            print(line)


if __name__ == '__main__':
    clize.run(main)
