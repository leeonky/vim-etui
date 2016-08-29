class MessageBox:
	def __init__(self, vi, title='', message='', height=10):
		self.vim = vi
		self.title = title
		self.message = message
		self.height = height

	def show(self):
		self.vim.command("botright %dnew %s" % (self.height, self.title.replace(' ', '\ ')))
		self.vim.set_local('buftype=nowrite bufhidden=wipe nobuflisted noswapfile nowrap nonumber')
		self.vim.current.buffer[:] = self.message.split("\n")

