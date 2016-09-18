from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, lines=[], colors=[], title='', height=10, keys=[], handler_name='', open_style=None):
		super(ListMenu, self).__init__(vim,
			open_style or DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.RowColumnContent(*lines),
			DropdownForm.LineHighlight(),
			DropdownForm.ClickableRow(keys, handler_name),
			DropdownForm.ColorRow(colors),
			DropdownForm.NavigateableRow(),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, '<C-C>'))

