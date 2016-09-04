from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, title, lines, height=10):
		super(ListMenu, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.LineHighlight(),
			DropdownForm.RowColumnContent(*lines),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, '<C-C>'))

