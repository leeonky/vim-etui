from mock import patch
from plugin.widgets.rich_message_box import RichMessageBox
from plugin.widgets.dropdown_form import DropdownForm
from plugin.tests.fake_vim import TestWithFakeVim

class TestRichMessageBox(TestWithFakeVim):

	@patch("plugin.widgets.dropdown_form.DropdownForm.DisableEdit.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.NormalForm.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.OpenShow.__init__")
	def test_create_with_right_properties(self, open_show_init, normal_form_init,
			disable_edit_init):
		open_show_init.return_value = None
		normal_form_init.return_value = None
		disable_edit_init.return_value = None

		RichMessageBox(self.vim, title='title', height=10)

		open_show_init.assert_called_with(DropdownForm.Position.Bottom, 10, 'title')
		normal_form_init.assert_called_with()
		disable_edit_init.assert_called_with()

	def test_append_one_rich_line(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['Hello'])
		self.vim.command.assert_any_call('highlight eui_rich_fg_black ctermfg=black guifg=black')
		self.vim.command.assert_any_call('syntax match eui_rich_fg_black start=/\%1c\%1l/ end=/\%6c\%1l/')
