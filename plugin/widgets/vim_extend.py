import types

class VimExtend:
	@staticmethod

	def extend(vim):
		def set_local(self, value):
			vim.command('setlocal ' + value)
		vim.set_local = types.MethodType(set_local, vim)
		return vim
