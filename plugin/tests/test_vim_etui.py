import unittest
import plugin.vim_etui as sut


class VimEtuiTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_etui_example()
        self.assertEqual("Happy Hacking!", result)
