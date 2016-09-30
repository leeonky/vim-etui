from dropdown_form import DropdownForm
from high_light import HighLight
from stateful_object import StatefulObject
import re

class RichMessageBox(DropdownForm, StatefulObject):
	ansi_regex = r"\033\[(\d+(;\d+)*)m"

	def __init__(self, vim, title='', height=10, open_where=DropdownForm.Position.Bottom):
		super(RichMessageBox, self).__init__(vim,
			DropdownForm.OpenShow(open_where, height, title),
			DropdownForm.NormalForm(),
			DropdownForm.DisableEdit())
		StatefulObject.__init__(self, title)
		self.vim = vim
		self.last_high_light = HighLight()
		self.last_position = None

	def append_rich(self, *rows):
		self.vim.set_local('modifiable')
		for row in rows:
			row_index = len(self.vim.current.buffer)+1

			match = re.search(RichMessageBox.ansi_regex, row)
			while(match):
				self._process_ansi_match(match.group(1), row_index, match.start()+1)
				row = row[:match.start()] + row[match.end():]
				match = re.search(RichMessageBox.ansi_regex, row)

			self.vim.current.buffer.append(row)
		self.vim.set_local('nomodifiable')

	def _process_ansi_match(self, ansi_code, row, col):
		def process_ansi_code(ansi_code):
			if 30 <= ansi_code < 40:
				self.last_high_light = self.last_high_light.change_to(fg=str(ansi_code-30))
			elif 90 <= ansi_code < 100:
				self.last_high_light = self.last_high_light.change_to(fg=str(ansi_code-90+8))
			elif 40 <= ansi_code < 50:
				self.last_high_light = self.last_high_light.change_to(bg=str(ansi_code-40))
			elif 100 <= ansi_code < 110:
				self.last_high_light = self.last_high_light.change_to(bg=str(ansi_code-100+8))
			elif ansi_code == 1:
				self.last_high_light = self.last_high_light.add_styles('bold')
			elif ansi_code == 4:
				self.last_high_light = self.last_high_light.add_styles('underline')
			elif ansi_code == 7:
				self.last_high_light = self.last_high_light.add_styles('inverse')
			elif ansi_code == 21:
				self.last_high_light = self.last_high_light.remove_styles('bold')
			elif ansi_code == 24:
				self.last_high_light = self.last_high_light.remove_styles('underline')
			elif ansi_code == 27:
				self.last_high_light = self.last_high_light.remove_styles('inverse')
			elif ansi_code == 0:
				self.last_high_light = self.last_high_light.change_to_reset()

		if self.last_position != (row, col):
			self.vim.high_light(self.last_high_light)
			self.vim.syntax_region(self.last_high_light, start=self.last_position, end=(row, col))
			self.last_position = (row, col)

		for ansi_code in ansi_code.split(';'):
			process_ansi_code(int(ansi_code))
