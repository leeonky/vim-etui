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

	def test_should_extend_map_local(self):
		VimExtend.extend(self.vim)

		self.vim.map_local('<cr>', ':q!<cr>')

		self.vim.command.assert_called_with('noremap <silent> <buffer> <cr> :q!<cr>');

	def test_should_extend_map_local_in_mulit_mappings(self):
		VimExtend.extend(self.vim)

		self.vim.map_local('<cr>', ':q!<cr>', 'noremap', 'vnoremap')

		self.vim.command.assert_any_call('noremap <silent> <buffer> <cr> :q!<cr>');
		self.vim.command.assert_any_call('vnoremap <silent> <buffer> <cr> :q!<cr>');

	def test_should_extend_map_many_local(self):
		VimExtend.extend(self.vim)

		self.vim.map_many_local(['<cr>'], ':q!<cr>')

		self.vim.command.assert_called_with('noremap <silent> <buffer> <cr> :q!<cr>');
