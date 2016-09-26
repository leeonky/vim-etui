import unittest
from mock import MagicMock
from plugin.widgets.fake_vim import TestWithFakeVim
from plugin.widgets.fake_vim import FakeVim
from plugin.widgets.vim_extend import VimExtend
from plugin.widgets.high_light import HighLight

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

	def test_extend_high_light(self):
		light = HighLight(styles=[HighLight.Bold])

		self.vim.high_light(light)

		self.vim.command.assert_called_with('highlight etui_hl_bold cterm=bold')

	def test_extend_none_high_light(self):
		light = HighLight()

		self.vim.high_light(light)

		self.assertEqual(self.vim.command.call_args_list, [])

	def test_extend_syntax_region_with_whole_line(self):
		light = HighLight(styles=[HighLight.Bold])

		self.vim.syntax_region(light, row=1)

		self.vim.command.assert_called_with('syntax region etui_hl_bold start=/\%1l/ end=/\%2l/')

	def test_extend_syntax_region_with_whole_line(self):
		light = HighLight(styles=[HighLight.Bold])

		self.vim.syntax_region(light, start=(1,2), end=(3,4))

		self.vim.command.assert_called_with('syntax region etui_hl_bold start=/\%1l\%2c/ end=/\%3l\%4c/')

	def test_extend_syntax_region_with_none_high_light(self):
		light = HighLight()

		self.vim.syntax_region(light, row=1)

		self.assertEqual(self.vim.command.call_args_list, [])

	def test_extend_current_postion(self):
		def fake_command(cmd):
			if cmd == "line('.')":
				return '2'
			if cmd == "col('.')":
				return '4'
		self.vim.eval = fake_command

		self.assertEqual((2, 4), self.vim.current_cursor())
