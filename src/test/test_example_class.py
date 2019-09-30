'''
test_example_class.py
Author: Michael Matthews
'''
import subprocess
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from main import ExampleClass


class TestExampleClass(unittest.TestCase):
    '''
    Tests for the ExampleClass.
    NOTE: Logging tests likely aren't necessary, these are just examples.
    '''
    def setUp(self):
        self.loggerPatch = patch('main.logger')
        self.mockLogger: MagicMock = self.loggerPatch.start()

    def test_run_logging(self): # pylint: disable=invalid-name
        '''
        Test simple logging.
        '''
        runParam = 'foo'
        ex = ExampleClass('hello', 'bye')
        with patch.object(subprocess, 'Popen'):
            ex.run(runParam)

        self.mockLogger.info.assert_any_call(f'Info message - {runParam}!')
        self.assertIn(runParam, self.mockLogger.info.call_args_list[0][0][0])

    @patch('subprocess.Popen.__enter__')
    def test_subprocess_out(self, mockPopen: MagicMock): # pylint: disable=invalid-name
        '''
        Test logging of Popen output
        '''
        commandStdOut = ['one', 'two']
        mockPopen.return_value = MagicMock(stdout=commandStdOut)
        runParam = 'foo'
        ex = ExampleClass('hello', 'bye')
        ex.run(runParam)

        self.mockLogger.info.assert_any_call(f'Out - {"".join(commandStdOut)}')

    @patch('subprocess.Popen')
    def test_command_build(self, mockPopen: MagicMock): # pylint: disable=invalid-name
        '''
        Test whether we built the command submitted to Popen correctly.
        '''
        runParam = 'foo'
        ex = ExampleClass('hello', 'bye')
        ex.run(runParam)

        self.assertEqual(mockPopen.call_args[0][0], ['ls', f'-{runParam}'])
