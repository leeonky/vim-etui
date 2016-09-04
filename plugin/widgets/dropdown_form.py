class DropdownForm(object):
	def __init__(self, vim, *properties):
		self.vim = vim
		self.properties = properties

	def show(self):
		for prop in self.properties:
			prop.update_property(self.vim) 

	class OpenNew(object):
		def __init__(self, position, size, title):
			self.position = position
			self.size = size
			self.title = title.replace(' ', '\ ')
		def update_property(self, vim):
			vim.command('silent %s %d%s %s' % (self.position[0], self.size, self.position[1], self.title))

	class OpenShow(object):
		def __init__(self, position, size, title):
			self.title = title
			self.open_new = DropdownForm.OpenNew(position, size, title)
		def update_property(self, vim):
			window_number = vim.window_number_of_buffer(self.title)
			if(window_number<0):
				self.open_new.update_property(vim)
			else:
				vim.command('%dwincmd w' % (window_number))

	class Position(object):
		Bottom = ('botright', 'new')
		Right = ('botright', 'vnew')

	class NormalForm(object):
		def update_property(self, vim):
			vim.set_local('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')

	class LineHighlight(object):
		def update_property(self, vim):
			vim.set_local('nocursorcolumn cursorline')

	class TextContent(object):
		def __init__(self, text):
			self.text = text
		def update_property(self, vim):
			vim.current.buffer[:] = self.text.split("\n")

	class RowColumnContent(object):
		def __init__(self, *lines):
			self.lines = list(lines)
		def update_property(self, vim):
			def max_width_for_each_column():
				max_widthes = [0] * len(self.lines[0])
				for line in self.lines:
					for col in list(enumerate(line)):
						max_widthes[col[0]] = max(max_widthes[col[0]], len(col[1]))
				return max_widthes
			def extend_column_to_fixed_width(max_widthes, line):
				return map(lambda width, col: ("%%-%ds" % (width))%(col), max_widthes, line)
			def join_column_with_tab(max_widthes):
				return map(lambda line: "\t".join(extend_column_to_fixed_width(max_widthes, line)), self.lines)
			vim.current.buffer[:] = join_column_with_tab(max_width_for_each_column())

	class DisableEdit(object):
		def update_property(self, vim):
			vim.set_local('nomodifiable')

	class CloseAndFocusBack(object):
		def __init__(self, old_window_number, key, *keys):
			self.old_window_number = old_window_number
			self.keys = [key] + list(keys)
		def update_property(self, vim):
			vim.map_many_local(self.keys, ":q!<CR>:%dwincmd w<CR>" % self.old_window_number)
