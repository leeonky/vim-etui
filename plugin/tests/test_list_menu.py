from mock import patch
from plugin.widgets.list_menu import ListMenu
from plugin.widgets.dropdown_form import DropdownForm
from plugin.widgets.fake_vim import TestWithFakeVim

class TestListMenu(TestWithFakeVim):

	@patch("plugin.widgets.dropdown_form.DropdownForm.CloseAndFocusBack.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.DisableEdit.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.NavigateableRow.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.ClickableBuffer.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.RowColumnContent.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.ColorRow.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.LineHighlight.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.NormalForm.__init__")
	@patch("plugin.widgets.dropdown_form.DropdownForm.OpenShow.__init__")
	def test_create_with_right_properties(self,
			open_show_init,
			normal_form_init,
			line_highlight_init,
			color_row_init,
			row_column_content_init,
			clickable_buffer_init,
			navigateable_row_init,
			disable_edit_init,
			close_and_focus_back_init):
		open_show_init.return_value = None
		normal_form_init.return_value = None
		line_highlight_init.return_value = None
		color_row_init.return_value = None
		row_column_content_init.return_value = None
		clickable_buffer_init.return_value = None
		navigateable_row_init.return_value = None
		disable_edit_init.return_value = None
		close_and_focus_back_init.return_value = None

		def handler_test(key):
			pass

		ListMenu(self.vim, title='title', height=11, lines=[['a'], ['b']], colors=['red', 'yellow'], keys=['c'], export_model='export', handler=handler_test, close_keys=['cc'])

		open_show_init.assert_called_with(DropdownForm.Position.Bottom, 11, 'title')
		normal_form_init.assert_called_with()
		line_highlight_init.assert_called_with()
		color_row_init.assert_called_with(['red', 'yellow'])
		row_column_content_init.assert_called_with(['a'], ['b'])
		clickable_buffer_init.assert_called_with(['c'], 'export', '__ListMenu_title', handler_test)
		navigateable_row_init.assert_called_with()
		disable_edit_init.assert_called_with()
		close_and_focus_back_init.assert_called_with(1, 'cc')
