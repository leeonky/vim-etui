import unittest
from mock import MagicMock
from mock import patch
from plugin.widgets.message_box import MessageBox
from plugin.widgets.dropdown_form import DropdownForm
from plugin.tests.fake_vim import FakeVim
from plugin.tests.fake_vim import FakeExtend

class TestMessageBox(unittest.TestCase):

	def setUp(self):
		self.vim = FakeExtend.extend(FakeVim.create())

	@patch("plugin.widgets.dropdown_form.DropdownForm.CloseAndFocusBack.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.TextContent.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.NormalForm.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.OpenNew.__init__")
	def test_create_with_right_properties(self, open_new_init, normal_form_init,
			text_content_init, close_and_focus_back_init):
		self.vim.current.window.number = 1
		open_new_init.return_value = None
		normal_form_init.return_value = None
		text_content_init.return_value = None
		close_and_focus_back_init.return_value = None

		MessageBox(self.vim, title='title', message='message', height=10)

		open_new_init.assert_called_with(DropdownForm.Position.Bottom, 10, 'title')
		normal_form_init.assert_called_with()
		text_content_init.assert_called_with('message')
		close_and_focus_back_init.assert_called_with(1, '<CR>', '<ESC>', '<C-C>')
