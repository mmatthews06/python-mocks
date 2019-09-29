
import unittest
from io import StringIO
from unittest.mock import patch
from unittest.mock import MagicMock

from main import ExampleClass

@patch('main.logger')
class TestMainMethod(unittest.TestCase):

    @patch('subprocess.Popen')
    def test_run_logging(self, mockPopen: MagicMock, mockLogger: MagicMock):
        '''
        Test simple logging.
        '''
        runParam = 'foo'
        ex = ExampleClass('hello', 'bye')
        ex.run(runParam)

        mockLogger.info.assert_any_call(f'Info message - {runParam}!')
        self.assertIn(runParam, mockLogger.info.call_args_list[0][0][0])

    @patch('subprocess.Popen.__enter__')
    def test_subprocess_out(self, mockPopen: MagicMock, mockLogger: MagicMock):
        '''
        Test logging of Popen output
        '''
        commandStdOut = ['one', 'two']
        mockPopen.return_value = MagicMock(stdout=commandStdOut)
        runParam = 'foo'
        ex = ExampleClass('hello', 'bye')
        ex.run(runParam)

        mockLogger.info.assert_any_call(f'Out - {"".join(commandStdOut)}')

    @patch('subprocess.Popen')
    def test_command_build(self, mockPopen: MagicMock, mockLogger: MagicMock):
        '''
        Test whether we built the command submitted to Popen correctly.
        '''
        runParam = 'foo'
        ex = ExampleClass('hello', 'bye')
        ex.run(runParam)

        self.assertEqual(mockPopen.call_args[0][0], ['ls', f'-{runParam}'])
