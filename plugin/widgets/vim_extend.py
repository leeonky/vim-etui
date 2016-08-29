import types

class VimExtend:
	@staticmethod

	def extend(vim):
		def set_local(self, value):
			vim.command('setlocal ' + value)
		vim.set_local = types.MethodType(set_local, vim)

		def map_local(self, key, action, *maps):
			if len(maps) == 0:
				maps = ['noremap']
			for _map in maps:
				vim.command('%s <silent> <buffer> %s %s' % (_map, key, action))
		vim.map_local = types.MethodType(map_local, vim)

		def map_many_local(self, keys, action, *maps):
			if len(maps) == 0:
				maps = ['noremap']
			for key in keys:
				for _map in maps:
					vim.command('%s <silent> <buffer> %s %s' % (_map, key, action))

		vim.map_many_local = types.MethodType(map_many_local, vim)

		return vim
