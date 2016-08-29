import unittest
from mock import MagicMock
from plugin.tests.fake_vim import FakeVim
from plugin.widgets.vim_extend import VimExtend

class TestVimExtend(unittest.TestCase):

	def setUp(self):
		self.vim = FakeVim.create()

	def test_should_extend_set_local(self):
		VimExtend.extend(self.vim)

		self.vim.set_local('hello=world')

		self.vim.command.assert_called_with('setlocal hello=world');
