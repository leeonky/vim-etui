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

		def window_number_of_buffer(self, title):
			return int(vim.eval("bufwinnr('^%s$')" % (title)))

		vim.window_number_of_buffer = types.MethodType(window_number_of_buffer, vim)

		def high_light(self, light):
			if not light.none_high_light():
				vim.command('highlight %s %s' % (light.name(), light.properties()))
		vim.high_light = types.MethodType(high_light, vim)

		def syntax_region(self, light, **args):
			if not light.none_high_light():
				if 'row' in args:
					row = args['row']
					vim.command("syntax region %s start=/\%%%dl/ end=/\%%%dl/" % (light.name(), row, row+1))
				if 'start' in args and 'end' in args:
					start = args['start']
					end = args['end']
					vim.command("syntax region %s start=/\%%%dl\%%%dc/ end=/\%%%dl\%%%dc/" % (light.name(), start[0], start[1], end[0], end[1]))
		vim.syntax_region = types.MethodType(syntax_region, vim)

		return vim
