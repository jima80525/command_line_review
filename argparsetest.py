#!/usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="*", help='log files to process')
    parser.add_argument("-l", "--limit", type=int, default=0,
                        help='Smallest value shown')
    parser.add_argument("-i", "--include", type=str,
                        help='Show only these comma separated commands')
    parser.add_argument("-e", "--exclude", type=str,
                        help='Exclude these comma separated commands')
    args = parser.parse_args()
    print('limit = {0}'.format(args.limit))
    if args.include:
        print('include passed: {0}'.format(args.include))
    if args.exclude:
        print('exclude passed: {0}'.format(args.exclude))
    for filename in args.input:
        with open(filename) as f:
            line = f.readline().strip()
            print(line)


if __name__ == '__main__':
    main()
