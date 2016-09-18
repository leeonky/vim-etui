from mock import patch
from mock import call
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
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_fg0 ctermfg=0 guifg=0'),
			call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/')])

	def test_append_one_line_with_two_high_lights(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[0m\033[31mHello\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['HelloHello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_fg0 ctermfg=0 guifg=0'),
			call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/'),
			call('highlight etui_hl_fg1 ctermfg=1 guifg=1'),
			call('syntax region etui_hl_fg1 start=/\%1l\%6c/ end=/\%1l\%11c/')])

	def test_append_one_line_with_change_high_light(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[40mHello\033[0m\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['HelloHello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_fg0 ctermfg=0 guifg=0'),
			call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/'),
			call('highlight etui_hl_fg0_bg0 ctermfg=0 guifg=0 ctermbg=0 guibg=0'),
			call('syntax region etui_hl_fg0_bg0 start=/\%1l\%6c/ end=/\%1l\%11c/')])

	def test_append_one_line_with_multi_high_light_in_two_ansi_code(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30m\033[40mHello\033[0m\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['Hello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_fg0_bg0 ctermfg=0 guifg=0 ctermbg=0 guibg=0'),
			call('syntax region etui_hl_fg0_bg0 start=/\%1l\%1c/ end=/\%1l\%6c/')])

	def test_append_one_line_with_multi_high_light_in_another_two_ansi_code(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[90m\033[100mHello\033[0m\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['Hello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_fg8_bg8 ctermfg=8 guifg=8 ctermbg=8 guibg=8'),
			call('syntax region etui_hl_fg8_bg8 start=/\%1l\%1c/ end=/\%1l\%6c/')])

	def test_append_one_line_with_styles(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[1m\033[4m\033[7mHello\033[21m\033[24m\033[27m\033[30mHello\033[0m\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['HelloHello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_bold_inverse_underline cterm=bold,inverse,underline'),
			call('syntax region etui_hl_bold_inverse_underline start=/\%1l\%1c/ end=/\%1l\%6c/'),
			call('highlight etui_hl_fg0 ctermfg=0 guifg=0'),
			call('syntax region etui_hl_fg0 start=/\%1l\%6c/ end=/\%1l\%11c/')])

	def test_append_one_line_with_multi_high_light_in_one_ansi_code(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[1;4;7mHello\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['Hello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_bold_inverse_underline cterm=bold,inverse,underline'),
			call('syntax region etui_hl_bold_inverse_underline start=/\%1l\%1c/ end=/\%1l\%6c/')])

	def test_append_one_line_with_special_ansi_code(self):
		box = RichMessageBox(self.vim, title='title')

		box.append_rich("\033[30mHello\033[0m")
		box.append_rich("\033[0;30mHello\033[0m")

		self.assertEqual(self.vim.current.buffer[:], ['Hello', 'Hello'])
		self.assertEqual(self.vim.command.call_args_list, [
			call('highlight etui_hl_fg0 ctermfg=0 guifg=0'),
			call('syntax region etui_hl_fg0 start=/\%1l\%1c/ end=/\%1l\%6c/'),
			call('highlight etui_hl_fg0 ctermfg=0 guifg=0'),
			call('syntax region etui_hl_fg0 start=/\%2l\%1c/ end=/\%2l\%6c/')])
