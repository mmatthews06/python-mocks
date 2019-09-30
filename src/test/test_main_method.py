'''
test_main_method.py
'''
import inspect
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from unittest.mock import MagicMock

import main as mainModule
from main import main


class TestMainMethod(unittest.TestCase):
    # pylint: disable=no-self-use
    '''
    Tests for the main method in main.py
    '''
    @patch('main.ExampleClass')
    def test_main_passes_foo(self, mockExampleClass: MagicMock): # pylint: disable=invalid-name
        '''
        Test if main passes the foo argument.
        '''
        foo = 'hello'
        args = ['main', '-f', foo]
        with  patch.object(sys, 'argv', args):
            main()
            mockExampleClass.assert_called_with(foo, None)

    @patch('main.ExampleClass')
    def test_main_passes_bar(self, mockExampleClass: MagicMock): # pylint: disable=invalid-name
        '''
        Test if main passes the bar argument.
        '''
        bar = 'bye'
        args = ['main', '-b', bar]
        with  patch.object(sys, 'argv', args):
            main()
            mockExampleClass.assert_called_with(None, bar)

    @patch('main.ExampleClass')
    def test_main_passes_foo_and_bar(self, mockExampleClass: MagicMock): # pylint: disable=invalid-name
        '''
        Test if main passes both arguments when provided (NOTE: not likely necessary)
        '''
        foo = 'hello'
        bar = 'bye'
        args = ['main', '-f', foo, '-b', bar]
        with  patch.object(sys, 'argv', args):
            main()
            mockExampleClass.assert_called_with(foo, bar)

    @patch('sys.argv', ['main', '-r'])
    @patch('main.ExampleClass.run')
    def test_main_runs_method(self, mockRunMethod: MagicMock): # pylint: disable=invalid-name
        '''
        Test if main calls the run method when `-r` is provided.
        '''
        defaultRunParam = 'not specified!'
        main()
        mockRunMethod.assert_called_with(defaultRunParam)

    @patch('main.ExampleClass.run')
    def test_main_runs_method_with_param(self, mockRunMethod: MagicMock): # pylint: disable=invalid-name
        '''
        Test if main passes the right parameter to the run method
        '''
        runParam = 'I am a run param!'
        args = ['main', '-r', '-p', runParam]
        with  patch.object(sys, 'argv', args):
            main()
            mockRunMethod.assert_called_with(runParam)

    @patch('sys.argv', ['main', '-v'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_display_version(self, mockStdOut: StringIO): # pylint: disable=invalid-name
        '''
        Test printing the version. Also demos expecting an assertion.
        (NOTE: possibly not needed, but nice to have.)
        '''
        with self.assertRaises(SystemExit):
            main()
        self.assertIn('main 1.0', mockStdOut.getvalue())

    def test_if_name_equals_main(self): # pylint: disable=invalid-name
        '''
        Test if the last lines are the canonical ones.
        (NOTE: I do not personally endorse this test, reasonable minds may differ.)
        '''
        sourceLines = inspect.getsourcelines(mainModule)[0]
        penultimateLine = sourceLines[-2]
        lastLine = sourceLines[-1]
        self.assertEqual(penultimateLine, "if __name__ == '__main__':\n")
        self.assertEqual(lastLine, "    main()\n")
