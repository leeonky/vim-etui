class MessageBox:
	def __init__(self, vi, title, message):
		self.vim = vi
		self.title = title
		self.message = message

	def show(self):
		self.vim.command("botright new " + self.title.replace(' ', '\ '))
		buffer_index = self.vim.eval("bufwinnr('^" + self.title + "$')")-1
		self.vim.command(str(buffer_index) + "wincmd w")

