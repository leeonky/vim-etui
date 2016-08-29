import unittest
from mock import MagicMock
from plugin.widgets.message_box import MessageBox
from plugin.tests.fake_vim import FakeVim
from plugin.tests.fake_vim import FakeExtend

class TestMessageBox(unittest.TestCase):

	def setUp(self):
		self.vim = FakeExtend.extend(FakeVim.create())


	def test_should_pop_up_a_full_width_widow_at_the_bottom_with_the_title(self):
		message_box = MessageBox(self.vim, 'Hello', 'World!')
		message_box.show()

		self.vim.command.assert_any_call('silent botright 10new Hello')

	def test_window_title_escape_the_space(self):
		message_box = MessageBox(self.vim, 'Hello Hello', 'World!')
		message_box.show()

		self.vim.command.assert_any_call('silent botright 10new Hello\ Hello')

	def test_should_message_with_height(self):
		message_box = MessageBox(self.vim, 'Hello Hello', 'World!', height=5)
		message_box.show()

		self.vim.command.assert_any_call('silent botright 5new Hello\ Hello')

	def test_buffer_should_has_the_right_options(self):
		message_box = MessageBox(self.vim, 'Hello Hello', 'World!')
		message_box.show()
		self.vim.set_local.assert_any_call('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')

	def test_should_output_message_to_buffer(self):
		message_box = MessageBox(self.vim, 'Hello Hello', 'World!')
		message_box.show()

		assert self.vim.current.buffer[:] == ['World!']

	def test_should_output_multi_line_message_to_buffer(self):
		message_box = MessageBox(self.vim, 'Hello', 'Hello\nWorld')
		message_box.show()

		assert self.vim.current.buffer[:] == ['Hello', 'World']

	def test_should_map_quit_shortcut(self):
		self.vim.current.window.number = 10

		message_box = MessageBox(self.vim, 'Hello', 'Hello\nWorld')
		message_box.show()

		self.vim.map_many_local.assert_called_with(['<CR>', '<ESC>'], ':q!<CR>:10wincmd w<CR>')
