from mock import patch
from plugin.widgets.list_menu import ListMenu
from plugin.widgets.dropdown_form import DropdownForm
from plugin.tests.fake_vim import TestWithFakeVim

class TestListMenu(TestWithFakeVim):

	@patch("plugin.widgets.dropdown_form.DropdownForm.OpenShow.__init__")
	def test_create_with_right_properties(self, open_show_init):
		open_show_init.return_value = None

		ListMenu(self.vim, title='title', height=10)

		open_show_init.assert_called_with(DropdownForm.Position.Bottom, 10, 'title')
