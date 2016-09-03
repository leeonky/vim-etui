import unittest
from mock import MagicMock
from mock import patch
from plugin.widgets.list_menu import ListMenu
from plugin.widgets.dropdown_form import DropdownForm
from plugin.tests.fake_vim import FakeVim
from plugin.tests.fake_vim import FakeExtend

class TestListMenu(unittest.TestCase):

	def setUp(self):
		self.vim = FakeExtend.extend(FakeVim.create())

	@patch("plugin.widgets.dropdown_form.DropdownForm.OpenShow.__init__")
	def test_create_with_right_properties(self, open_show_init):
		self.vim.current.window.number = 1
		open_show_init.return_value = None

		ListMenu(self.vim, title='title', height=10)

		open_show_init.assert_called_with(DropdownForm.Position.Bottom, 10, 'title')
