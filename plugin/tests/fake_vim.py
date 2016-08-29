from mock import MagicMock

class FakeCurrent:

	@staticmethod
	def create():
		current = FakeCurrent()
		current.buffer = []
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
		vim.set_local = MagicMock()
		vim.map_local = MagicMock()
		vim.map_many_local = MagicMock()
		return vim
