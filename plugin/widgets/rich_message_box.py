from dropdown_form import DropdownForm
from plugin.widgets.high_light import HighLight
import re

class RichMessageBox(DropdownForm):
	def __init__(self, vim, title='', height=10):
		self.vim = vim
		super(RichMessageBox, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.DisableEdit())

	def append_rich(self, row):
		self.vim.current.buffer.append(row)
		# row_index = len(self.vim.current.buffer)+1
		# re.search(r"\033\[\d+(;\d+)*m", row)
		# self.vim.current.buffer.append('Hello')
		# light = HighLight(fg='0')
		# self.vim.high_light(light)
		# self.vim.syntax_region(light, start=(row_index, 1), end=(row_index, 6))
