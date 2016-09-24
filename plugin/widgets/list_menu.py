from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, lines=[], colors=[], title='', height=10, open_where=DropdownForm.Position.Bottom, keys=[], handler_name='', close_keys=[]):
		super(ListMenu, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 11, title),
			DropdownForm.NormalForm(),
			DropdownForm.RowColumnContent(*lines),
			DropdownForm.LineHighlight(),
			DropdownForm.ClickableRow(keys, handler_name),
			DropdownForm.ColorRow(colors),
			DropdownForm.NavigateableRow(),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, *close_keys))

