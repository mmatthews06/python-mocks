#!/bin/env/python3
'''
main.py
Author: Michael Matthews
'''
import argparse
import logging
import subprocess
import sys


logger = logging.getLogger(__name__) # pylint: disable=invalid-name
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class ExampleClass(): # pylint: disable=too-few-public-methods
    '''
    A class to demonstrate some moderately complicated mocks.
    '''
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
        self.baseCommand = 'ls'

    def run(self, param):
        '''
        Generic "run" method for this example class. Features:
        1. logs using logger.
        2. subprocess.Popen for mocking later.
        '''
        logger.info(f'Info message - {param}!')

        command = [self.baseCommand, f'-{param}']
        stdoutStr = ''
        with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:
            for line in proc.stdout:
                stdoutStr += str(line)

        logger.info(f'Out - {stdoutStr}')


def parseArgs():
    '''
    Simple argument parsing method.
    '''
    parser = argparse.ArgumentParser(description='Example Class for demonstrating python mocks')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-f', '--foo')
    parser.add_argument('-b', '--bar')
    parser.add_argument('-r', '--run', action='store_true', default=False)
    parser.add_argument('-p', '--param', default='not specified!')

    return parser.parse_args()

def main():
    '''
    main method, to demonstrate mocking pieces it will use.
    '''
    args = parseArgs()
    example = ExampleClass(args.foo, args.bar)

    if args.run:
        example.run(args.param)


if __name__ == '__main__':
    main()
