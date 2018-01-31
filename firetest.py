#!/usr/bin/env python
import fire

def main(*logfiles, limit=0, include='', exclude=''):
    print('limit = {0}'.format(limit))
    if include:
        print('include passed: {0}'.format(include))
    if exclude:
        print('exclude passed: {0}'.format(exclude))
    for filename in logfiles:
        with open(filename) as f:
            line = f.readline().strip()
            print(line)


if __name__ == '__main__':
    fire.Fire(main)
