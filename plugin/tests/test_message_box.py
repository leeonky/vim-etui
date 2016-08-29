import unittest
from mock import MagicMock
from plugin.widgets.message_box import MessageBox

class FakeVim:

	def __inid__(self):
		pass

	@staticmethod
	def create():
		vim = FakeVim()
		vim.command = MagicMock()
		vim.eval = MagicMock()
		return vim

class TestMessageBox(unittest.TestCase):

	def test_should_pop_up_a_full_width_widow_at_the_bottom_with_the_title(self):
		vim = FakeVim.create()

		message_box = MessageBox(vim, 'Hello', 'World!')
		message_box.show()

		vim.command.assert_any_call('botright new Hello')

	def test_window_title_escape_the_space(self):
		vim = FakeVim.create()

		message_box = MessageBox(vim, 'Hello Hello', 'World!')
		message_box.show()

		vim.command.assert_any_call('botright new Hello\ Hello')

	def test_should_change_focus_to_new_window(self):
		vim = FakeVim.create()
		vim.eval.return_value = 5

		message_box = MessageBox(vim, 'Hello Hello', 'World!')
		message_box.show()

		vim.eval.assert_any_call("bufwinnr('^Hello Hello$')")
		vim.command.assert_any_call("4wincmd w")

