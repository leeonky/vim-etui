import unittest
from mock import MagicMock
from plugin.tests.fake_vim import TestWithFakeVim
from plugin.tests.fake_vim import FakeVim
from plugin.widgets.vim_extend import VimExtend

class TestVimExtend(unittest.TestCase):

	def setUp(self):
		self.vim = VimExtend.extend(FakeVim.create())

	def test_should_extend_set_local(self):
		self.vim.set_local('hello=world')

		self.vim.command.assert_called_with('setlocal hello=world');

	def test_should_extend_map_local(self):
		self.vim.map_local('<cr>', ':q!<cr>')

		self.vim.command.assert_called_with('noremap <silent> <buffer> <cr> :q!<cr>');

	def test_should_extend_map_local_in_mulit_mappings(self):
		self.vim.map_local('<cr>', ':q!<cr>', 'noremap', 'vnoremap')

		self.vim.command.assert_any_call('noremap <silent> <buffer> <cr> :q!<cr>');
		self.vim.command.assert_any_call('vnoremap <silent> <buffer> <cr> :q!<cr>');

	def test_should_extend_map_many_local(self):
		self.vim.map_many_local(['<cr>'], ':q!<cr>')

		self.vim.command.assert_called_with('noremap <silent> <buffer> <cr> :q!<cr>');

	def test_should_extend_window_number_of_buffer(self):
		self.vim.window_number_of_buffer('hello')

		self.vim.eval.assert_called_with("bufwinnr('^hello$')");

	def test_window_number_of_buffer_should_return_number(self):
		self.vim.eval = MagicMock(return_value = '1')

		self.assertEqual(1, self.vim.window_number_of_buffer('hello'))


