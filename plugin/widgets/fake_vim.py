from mock import MagicMock
from vim_extend  import VimExtend
import unittest

class FakeWindow:
	@staticmethod
	def create():
		window = FakeWindow()
		window.number = 1
		return window

class FakeCurrent:

	@staticmethod
	def create():
		current = FakeCurrent()
		current.buffer = []
		current.window = FakeWindow.create()
		return current

class FakeVim:

	@staticmethod
	def create():
		vim = FakeVim()
		vim.command = MagicMock()
		vim.eval = MagicMock()
		vim.current = FakeCurrent.create()
		return vim

class FakeExtend:

	@staticmethod
	def extend(vim):
		vim = VimExtend.extend(vim)
		vim.set_local = MagicMock()
		vim.map_local = MagicMock()
		vim.map_many_local = MagicMock()
		vim.window_number_of_buffer = MagicMock()
		return vim

class TestWithFakeVim(unittest.TestCase):

	def setUp(self):
		self._vim = FakeExtend.extend(FakeVim.create())

	@property
	def vim(self):
		return self._vim

