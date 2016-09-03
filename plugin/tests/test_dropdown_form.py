from mock import MagicMock
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

		self.vim.command.assert_any_call('silent botright 10new Hello')

	def test_window_title_escape_the_space(self):
		prop = DropdownForm.OpenNew(position=DropdownForm.Position.Right, size=10, title='Hello Hello')

		prop.update_property(self.vim)

		self.vim.command.assert_any_call('silent botright 10vnew Hello\ Hello')

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

		self.vim.set_local.assert_any_call('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')

class TestTextContent(TestWithFakeVim):

	def test_should_output_message_to_buffer(self):
		prop = DropdownForm.TextContent('World!')

		prop.update_property(self.vim)

		self.assertEqual(['World!'], self.vim.current.buffer[:])

	def test_should_output_multi_line_message_to_buffer(self):
		prop = DropdownForm.TextContent('Hello\nWorld')

		prop.update_property(self.vim)

		assert self.vim.current.buffer[:] == ['Hello', 'World']

class TestDisableEdit(TestWithFakeVim):

	def test_should_set_nomodifiable(self):
		prop = DropdownForm.DisableEdit()

		prop.update_property(self.vim)

		self.vim.set_local.assert_any_call('nomodifiable')

class TestCloseAndFocusBack(TestWithFakeVim):

	def test_should_map_quit_shortcut(self):
		prop = DropdownForm.CloseAndFocusBack(10, '<CR>', '<ESC>', '<C-C>')

		prop.update_property(self.vim)

		self.vim.map_many_local.assert_called_with(['<CR>', '<ESC>', '<C-C>'], ':q!<CR>:10wincmd w<CR>')

