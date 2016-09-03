class DropdownForm(object):
	def __init__(self, vim, *properties):
		self.vim = vim
		self.properties = properties

	def show(self):
		for prop in self.properties:
			prop.update_property(self.vim) 

	class OpenNew(object):
		def __init__(self, position, size, title):
			self.position = {
					DropdownForm.Position.Bottom: 'botright',
					DropdownForm.Position.Right: 'botright'
					}[position]
			self.size = size
			self.new = {
					DropdownForm.Position.Bottom: 'new',
					DropdownForm.Position.Right: 'vnew'
					}[position]
			self.title = title.replace(' ', '\ ')
			pass
		def update_property(self, vim):
			vim.command('silent %s %d%s %s' % (self.position, self.size, self.new, self.title))

	class Position(object):
		Bottom = 1
		Right = 2

	class NormalForm(object):
		def update_property(self, vim):
			vim.set_local('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')

	class TextContent(object):
		def __init__(self, text):
			self.text = text
		def update_property(self, vim):
			vim.current.buffer[:] = self.text.split("\n")

	class CloseAndFocusBack(object):
		def __init__(self, old_window_number, key, *keys):
			self.old_window_number = old_window_number
			self.keys = [key] + list(keys)
		def update_property(self, vim):
			vim.map_many_local(self.keys, ":q!<CR>:%dwincmd w<CR>" % self.old_window_number)
