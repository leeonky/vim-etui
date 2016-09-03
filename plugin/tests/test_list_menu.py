import unittest
from mock import MagicMock
from plugin.widgets.list_menu import ListMenu
from plugin.tests.fake_vim import FakeVim
from plugin.tests.fake_vim import FakeExtend

class TestListMenu(unittest.TestCase):

	def setUp(self):
		self.vim = FakeExtend.extend(FakeVim.create())

