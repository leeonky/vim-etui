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
			def max_column_count():
				return max(map(lambda cols: len(cols), self.lines))
			def max_width_for_each_column():
				max_widthes = [0] * max_column_count()
				for cols in self.lines:
					for index, col in list(enumerate(cols)):
						max_widthes[index] = max(max_widthes[index], len(col))
				return max_widthes
			def extend_column_to_fixed_width(max_widthes, cols):
				return map(lambda width, col: ("%%-%ds" % (width))%(col), max_widthes[:len(cols)], cols)
			def join_column_with_tab(max_widthes):
				return map(lambda cols: "\t".join(extend_column_to_fixed_width(max_widthes, cols)), self.lines)
			vim.current.buffer[:] = join_column_with_tab(max_width_for_each_column())

	class ColorRow(object):
		def __init__(self, fg_colors, bg_colors=[]):
			self.fg_colors = fg_colors
			self.bg_colors = bg_colors
		def update_property(self, vim):
			def back_color_command(fg_color_index):
				if len(self.bg_colors)>0:
					bg_color = self.bg_colors[fg_color_index%len(self.bg_colors)]
					return ' ctermbg=%s guibg=%s' % (bg_color, bg_color)
				return ''
			def font_color_command(color):
				return 'ctermfg=%s guifg=%s' % (color, color)
			for index, color in list(enumerate(self.fg_colors)):
				vim.command('highlight eui_line_%s %s%s' % (color, font_color_command(color), back_color_command(index)))
			for line_number in range(0, len(vim.current.buffer)):
				vim.command("syntax region eui_line_%s start=/\%%%dl/ end=/\%%%dl/" % (self.fg_colors[line_number%len(self.fg_colors)], line_number+1, line_number+2))

	class DisableEdit(object):
		def update_property(self, vim):
			vim.set_local('nomodifiable')

	class CloseAndFocusBack(object):
		def __init__(self, old_window_number, key, *keys):
			self.old_window_number = old_window_number
			self.keys = [key] + list(keys)
		def update_property(self, vim):
			vim.map_many_local(self.keys, ":q!<CR>:%dwincmd w<CR>" % self.old_window_number)
