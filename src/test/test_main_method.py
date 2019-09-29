
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
        foo = 'hello'
        args = ['main', '-f', foo]
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(foo, None)

    @patch('main.ExampleClass')
    def test_main_passes_bar(self, MockExampleClass: MagicMock):
        bar = 'bye'
        args = ['main', '-b', 'bye']
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(None, bar)

    @patch('main.ExampleClass')
    def test_main_passes_foo_and_bar(self, MockExampleClass: MagicMock):
        foo = 'hello'
        bar = 'bye'
        args = ['main', '-f', foo, '-b', bar]
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(foo, bar)

    @patch('main.ExampleClass.run')
    def test_main_runs_method(self, MockRunMethod: MagicMock):
        defaultRunParam = 'not specified!'
        args = ['main', '-r']
        with  patch.object(sys, 'argv', args):
            main()
            MockRunMethod.assert_called_with(defaultRunParam)

    @patch('main.ExampleClass.run')
    def test_main_runs_method_with_param(self, MockRunMethod: MagicMock):
        runParam = 'I am a run param!'
        args = ['main', '-r', '-p', runParam]
        with  patch.object(sys, 'argv', args):
            main()
            MockRunMethod.assert_called_with(runParam)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_version(self, mockStdOut: StringIO):
        args = ['main', '-v']
        with  patch.object(sys, 'argv', args):
            with self.assertRaises(SystemExit):
                main()
            self.assertIn('main 1.0', mockStdOut.getvalue())
