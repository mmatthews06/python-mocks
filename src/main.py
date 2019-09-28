#!/bin/env/python3

class ExampleClass(object):
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Example Class for demonstrating python mocks')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-f', '--foo')
    parser.add_argument('-b', '--bar')

    return parser.parse_args()

def main():
    args = parse_args()
    example = ExampleClass(args.foo, args.bar)


if __name__ == '__main__':
    main()
