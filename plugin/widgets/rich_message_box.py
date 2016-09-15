from dropdown_form import DropdownForm

class RichMessageBox(DropdownForm):
	def __init__(self, vim, title='', height=10):
		self.vim = vim
		super(RichMessageBox, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.DisableEdit())

	def append_rich(self, row):
		row_index = len(self.vim.current.buffer)+1
		self.vim.current.buffer.append('Hello')
		self.vim.command('highlight eui_rich_fg_black ctermfg=black guifg=black')
		self.vim.command('syntax match eui_rich_fg_black start=/\%%1c\%%%dl/ end=/\%%6c\%%%dl/' % (row_index, row_index))
