from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, title, height, lines):
		super(ListMenu, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.LineHighlight(),
			DropdownForm.RowColumnContent(lines),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, '<CR>', '<ESC>', '<C-C>'))
