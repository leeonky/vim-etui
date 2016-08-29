class MessageBox:
	def __init__(self, vi, title='', message='', height=10):
		self.vim = vi
		self.title = title
		self.message = message
		self.height = height

	def show(self):
		old_window_number = self.vim.current.window.number
		self.vim.command("silent botright %dnew %s" % (self.height, self.title.replace(' ', '\ ')))
		self.vim.set_local('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')
		self.vim.current.buffer[:] = self.message.split("\n")
		self.vim.map_many_local(['<CR>', '<ESC>', '<C-C>'], ":q!<CR>:%dwincmd w<CR>" % old_window_number)

