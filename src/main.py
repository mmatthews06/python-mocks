#!/bin/env/python3

class ExampleClass(object):
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

    def run(self, param):
        pass


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Example Class for demonstrating python mocks')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-f', '--foo')
    parser.add_argument('-b', '--bar')
    parser.add_argument('-r', '--run', action='store_true', default=False)
    parser.add_argument('-p', '--param', default='not specified!')

    return parser.parse_args()

def main():
    args = parse_args()
    example = ExampleClass(args.foo, args.bar)

    if args.run:
        example.run(args.param)


if __name__ == '__main__':
    main()
