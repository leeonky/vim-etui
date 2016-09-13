import unittest
from plugin.widgets.libs.extended_int import ExtendedInt

class TestExtendedInt(unittest.TestCase):

	def test_0_alphabet_is_a(self):
		self.assertEqual('a', ExtendedInt(0).to_alphabet())

	def test_1_alphabet_is_b(self):
		self.assertEqual('b', ExtendedInt(1).to_alphabet())

	def test_26_alphabet_is_ba(self):
		self.assertEqual('ba', ExtendedInt(26).to_alphabet())

	def test_27_alphabet_is_ba(self):
		self.assertEqual('bb', ExtendedInt(27).to_alphabet())

	def test_52_alphabet_is_ca(self):
		self.assertEqual('ca', ExtendedInt(52).to_alphabet())

	def test_676_alphabet_is_ca(self):
		self.assertEqual('baa', ExtendedInt(676).to_alphabet())
