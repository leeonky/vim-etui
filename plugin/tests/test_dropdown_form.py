from mock import patch
from mock import MagicMock
from mock import call
from plugin.widgets.dropdown_form import DropdownForm
from plugin.tests.fake_vim import TestWithFakeVim

class TestDropdownForm(TestWithFakeVim):

	def test_should_show_with_all_properties(self):
		class Prop1:
			pass
		class Prop2:
			pass

		prop1 = Prop1()
		prop1.update_property = MagicMock()
		prop2 = Prop2()
		prop2.update_property = MagicMock()
		vim = self.vim

		class TestDropdownForm(DropdownForm):
			def __init__(self):
				super(TestDropdownForm, self).__init__(vim, prop1, prop2)

		TestDropdownForm().show()

		prop1.update_property.assert_called_with(vim)
		prop2.update_property.assert_called_with(vim)

class TestOpenNew(TestWithFakeVim):

	def test_should_pop_up_a_full_width_widow_at_the_bottom_with_the_title(self):
		prop = DropdownForm.OpenNew(position=DropdownForm.Position.Bottom, size=10, title='Hello')

		prop.update_property(self.vim)

		self.vim.command.assert_called_with('silent botright 10new Hello')

	def test_window_title_escape_the_space(self):
		prop = DropdownForm.OpenNew(position=DropdownForm.Position.Right, size=10, title='Hello Hello')

		prop.update_property(self.vim)

		self.vim.command.assert_called_with('silent botright 10vnew Hello\ Hello')

class TestOpenShow(TestWithFakeVim):

	def test_should_open_new_if_no_samed_title_form(self):
		self.vim.window_number_of_buffer.return_value = -1
		prop = DropdownForm.OpenShow(position=DropdownForm.Position.Right, size=10, title='Hello Hello')

		prop.update_property(self.vim)

		self.vim.command.assert_called_with('silent botright 10vnew Hello\ Hello')

	def test_should_open_new_if_no_samed_title_form(self):
		self.vim.window_number_of_buffer.return_value = 1
		prop = DropdownForm.OpenShow(position=DropdownForm.Position.Right, size=10, title='Hello Hello')

		prop.update_property(self.vim)

		self.vim.command.assert_called_with('1wincmd w')

class TestNormalForm(TestWithFakeVim):

	def test_buffer_should_has_the_right_options(self):
		prop = DropdownForm.NormalForm()

		prop.update_property(self.vim)

		self.vim.set_local.assert_called_with('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')

class TestLineHighlight(TestWithFakeVim):

	def test_buffer_should_has_the_right_options(self):
		prop = DropdownForm.LineHighlight()

		prop.update_property(self.vim)

		self.vim.set_local.assert_called_with('nocursorcolumn cursorline')

class TestTextContent(TestWithFakeVim):

	def test_should_output_message_to_buffer(self):
		prop = DropdownForm.TextContent('World!')

		prop.update_property(self.vim)

		self.assertEqual(['World!'], self.vim.current.buffer[:])

	def test_should_output_multi_line_message_to_buffer(self):
		prop = DropdownForm.TextContent('Hello\nWorld')

		prop.update_property(self.vim)

		assert self.vim.current.buffer[:] == ['Hello', 'World']

class TestRowColumnContent(TestWithFakeVim):

	def test_should_output_cell_join_with_tab(self):
		prop = DropdownForm.RowColumnContent(['A01', 'Hello'], ['A25', 'World'])

		prop.update_property(self.vim)

		self.assertEqual(["A01\tHello", "A25\tWorld"], self.vim.current.buffer[:])

	def test_should_append_space_to_same_width_before_join(self):
		prop = DropdownForm.RowColumnContent(['A0', 'Hello'], ['A25', 'World'])

		prop.update_property(self.vim)

		self.assertEqual(["A0 \tHello", "A25\tWorld"], self.vim.current.buffer[:])

	def test_with_different_columns(self):
		prop = DropdownForm.RowColumnContent(['A25'], ['A0', 'abc'])

		prop.update_property(self.vim)

		self.assertEqual(["A25", "A0 \tabc"], self.vim.current.buffer[:])

class TestColorRow(TestWithFakeVim):

	def setUp(self):
		super(TestColorRow, self).setUp()
		self.vim.current.buffer = ['a', 'b']

	def test_should_only_set_fg_color(self):
		prop = DropdownForm.ColorRow(['red', 'blue'])

		prop.update_property(self.vim)

		self.assertEqual(self.vim.command.call_args_list, [
				call('highlight eui_line_red ctermfg=red guifg=red'),
				call('highlight eui_line_blue ctermfg=blue guifg=blue'),
				call('syntax region eui_line_red start=/\%1l/ end=/\%2l/'),
				call('syntax region eui_line_blue start=/\%2l/ end=/\%3l/')])

	def test_should_only_set_fg_color_and_bg_color(self):
		prop = DropdownForm.ColorRow(['red', 'blue'], ['write', 'black'])

		prop.update_property(self.vim)

		self.assertEqual(self.vim.command.call_args_list, [
				call('highlight eui_line_red ctermfg=red guifg=red ctermbg=write guibg=write'),
				call('highlight eui_line_blue ctermfg=blue guifg=blue ctermbg=black guibg=black'),
				call('syntax region eui_line_red start=/\%1l/ end=/\%2l/'),
				call('syntax region eui_line_blue start=/\%2l/ end=/\%3l/')])

	def test_should_only_set_fg_color_and_one_bg_color(self):
		prop = DropdownForm.ColorRow(['red', 'blue'], ['write'])

		prop.update_property(self.vim)

		self.assertEqual(self.vim.command.call_args_list, [
				call('highlight eui_line_red ctermfg=red guifg=red ctermbg=write guibg=write'),
				call('highlight eui_line_blue ctermfg=blue guifg=blue ctermbg=write guibg=write'),
				call('syntax region eui_line_red start=/\%1l/ end=/\%2l/'),
				call('syntax region eui_line_blue start=/\%2l/ end=/\%3l/')])

class TestDisableEdit(TestWithFakeVim):

	def test_should_set_nomodifiable(self):
		prop = DropdownForm.DisableEdit()

		prop.update_property(self.vim)

		self.vim.set_local.assert_called_with('nomodifiable')

class TestClickableLine(TestWithFakeVim):

	def test_should_set_map_with_inter(self):
		handler_name = 'list_clicked'
		prop = DropdownForm.ClickableLine(['o', 's'], handler_name)

		prop.update_property(self.vim)

		self.vim.map_local.assert_any_call('o', ":call EUIClickableLineHandeler('o', '%s')<cr>" % handler_name)
		self.vim.map_local.assert_any_call('s', ":call EUIClickableLineHandeler('s', '%s')<cr>" % handler_name)


class TestCloseAndFocusBack(TestWithFakeVim):

	def test_should_map_quit_shortcut(self):
		prop = DropdownForm.CloseAndFocusBack(10, '<CR>', '<ESC>', '<C-C>')

		prop.update_property(self.vim)

		self.vim.map_many_local.assert_called_with(['<CR>', '<ESC>', '<C-C>'], ':q!<CR>:10wincmd w<CR>')

