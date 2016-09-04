from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, title, lines, colors=[], height=10):
		super(ListMenu, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.RowColumnContent(*lines),
			DropdownForm.DisableEdit(),
			DropdownForm.LineHighlight(),
			DropdownForm.ColorRow(colors),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, '<C-C>'))

