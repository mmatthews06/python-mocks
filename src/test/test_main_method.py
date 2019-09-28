
import sys
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

from main import main
from main import ExampleClass

class Test_Main(unittest.TestCase):

    @patch('main.ExampleClass')
    def test_main_passes_foo(self, MockExampleClass: MagicMock):
        args = ['main', '-f', 'hello']
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with('hello', None)

    @patch('main.ExampleClass')
    def test_main_passes_bar(self, MockExampleClass: MagicMock):
        args = ['main', '-b', 'bye']
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with(None, 'bye')

    @patch('main.ExampleClass')
    def test_main_passes_foo_and_bar(self, MockExampleClass: MagicMock):
        args = ['main', '-f', 'hello', '-b', 'bye']
        with  patch.object(sys, 'argv', args):
            main()
            MockExampleClass.assert_called_with('hello', 'bye')
