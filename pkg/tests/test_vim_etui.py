import unittest
import pkg.plugin.vim_etui as sut


@unittest.skip("Don't forget to test!")
class VimEtuiTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_etui_example()
        self.assertEqual("Happy Hacking", result)
