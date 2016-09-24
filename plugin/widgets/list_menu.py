from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, lines=[], colors=[], title='', height=10, open_where=DropdownForm.Position.Bottom, keys=[], export_model='', handler=None, close_keys=[]):
		super(ListMenu, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, height, title),
			DropdownForm.NormalForm(),
			DropdownForm.RowColumnContent(*lines),
			DropdownForm.LineHighlight(),
			DropdownForm.ClickableBuffer(keys, export_model, '__ListMenu_%s' % title, handler),
			DropdownForm.ColorRow(colors),
			DropdownForm.NavigateableRow(),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, *close_keys))

