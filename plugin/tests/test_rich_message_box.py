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

	def test_append_line_without_high_light(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("Hello")

		self.assertEqual(self.vim.current.buffer[:], ['Hello'])

	def test_append_one_line_with_high_light(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['Hello'])
		self.vim.command.assert_any_call('highlight etui_hl_fg0 ctermfg=0 guifg=0')
		self.vim.command.assert_any_call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/')

	def test_append_one_line_with_two_high_lights(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[0m\033[31mHello\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['HelloHello'])
		self.vim.command.assert_any_call('highlight etui_hl_fg0 ctermfg=0 guifg=0')
		self.vim.command.assert_any_call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/')
		self.vim.command.assert_any_call('highlight etui_hl_fg1 ctermfg=1 guifg=1')
		self.vim.command.assert_any_call('syntax region etui_hl_fg1 start=/\%1l\%6c/ end=/\%1l\%11c/')

	def test_append_one_line_with_change_high_light(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[40mHello\033[0m\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['HelloHello'])
		self.vim.command.assert_any_call('highlight etui_hl_fg0 ctermfg=0 guifg=0')
		self.vim.command.assert_any_call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/')
		self.vim.command.assert_any_call('highlight etui_hl_fg0_bg0 ctermfg=0 guifg=0 ctermbg=0 guibg=0')
		self.vim.command.assert_any_call('syntax region etui_hl_fg0_bg0 start=/\%1l\%6c/ end=/\%1l\%11c/')
