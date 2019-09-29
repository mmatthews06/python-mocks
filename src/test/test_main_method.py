
import inspect
import sys
import unittest
from io import StringIO
from unittest.mock import patch
from unittest.mock import MagicMock

from main import main
from main import ExampleClass

class TestMainMethod(unittest.TestCase):

    @patch('main.ExampleClass')
    def test_main_passes_foo(self, MockExampleClass: MagicMock):
        '''
        Test if main passes the foo argument.
        '''
        foo = 'hello'
        args = ['main', '-f', foo]
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(foo, None)

    @patch('main.ExampleClass')
    def test_main_passes_bar(self, MockExampleClass: MagicMock):
        '''
        Test if main passes the bar argument.
        '''
        bar = 'bye'
        args = ['main', '-b', 'bye']
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(None, bar)

    @patch('main.ExampleClass')
    def test_main_passes_foo_and_bar(self, MockExampleClass: MagicMock):
        '''
        Test if main passes both arguments when provided (NOTE: not likely necessary)
        '''
        foo = 'hello'
        bar = 'bye'
        args = ['main', '-f', foo, '-b', bar]
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(foo, bar)

    @patch('sys.argv', ['main', '-r'])
    @patch('main.ExampleClass.run')
    def test_main_runs_method(self, mockRunMethod: MagicMock):
        '''
        Test if main calls the run method when `-r` is provided.
        '''
        defaultRunParam = 'not specified!'
        main()
        mockRunMethod.assert_called_with(defaultRunParam)

    @patch('main.ExampleClass.run')
    def test_main_runs_method_with_param(self, mockRunMethod: MagicMock):
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
    def test_display_version(self, mockStdOut: StringIO):
        '''
        Test printing the version. Also demos expecting an assertion.
        (NOTE: possibly not needed, but nice to have.)
        '''
        with self.assertRaises(SystemExit):
            main()
        self.assertIn('main 1.0', mockStdOut.getvalue())

    def test_if_name_equals_main(self):
        '''
        Test if the last lines are the canonical ones.
        (NOTE: I do not personally endorse this test, reasonable minds may differ.)
        '''
        import main as mainModule
        sourceLines = inspect.getsourcelines(mainModule)[0]
        penultimateLine = sourceLines[-2]
        lastLine = sourceLines[-1]
        self.assertEqual(penultimateLine, "if __name__ == '__main__':\n")
        self.assertEqual(lastLine, "    main()\n")

