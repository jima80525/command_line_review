#!/usr/bin/env python
import plac


def main(
    include: ('Show only these comma separated commands', 'option', 'i')=None,
    exclude: ('Exclude these comma separated commands', 'option', 'e')=None,
    limit:   ('Smallest value shown', 'option', 'l', int)=0,
    *input:  ('log files to process')):
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
    plac.call(main)
