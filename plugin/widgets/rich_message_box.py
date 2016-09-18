from dropdown_form import DropdownForm
from plugin.widgets.high_light import HighLight
import re

class RichMessageBox(DropdownForm):
	def __init__(self, vim, title='', height=10):
		super(RichMessageBox, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.DisableEdit())
		self.vim = vim
		self.last_high_light = HighLight()
		self.last_position = None
	ansi_regex = r"\033\[(\d+(;\d+)*)m"

	def append_rich(self, row):
		row_index = len(self.vim.current.buffer)+1

		match = re.search(RichMessageBox.ansi_regex, row)
		while(match):
			self._process_ansi_match(match.group(1), row_index, match.start()+1)
			row = row[:match.start()] + row[match.end():]
			match = re.search(RichMessageBox.ansi_regex, row)

		self.vim.current.buffer.append(row)

	def _process_ansi_match(self, ansi_code, row, col):
		self.vim.high_light(self.last_high_light)
		self.vim.syntax_region(self.last_high_light, start=self.last_position, end=(row, col))
		self.last_position = (row, col)
		if ansi_code=='30':
			self.last_high_light = HighLight(fg='0')
		if ansi_code=='31':
			self.last_high_light = HighLight(fg='1')
		if ansi_code=='40':
			self.last_high_light = self.last_high_light.change_to(bg='0')
		elif ansi_code=='0':
			self.last_high_light = HighLight()
			self.last_position = None

