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
