from dropdown_form import DropdownForm

class MessageBox(DropdownForm):
	def __init__(self, vim, message='', title='', height=10, open_where=DropdownForm.Position.Bottom, close_keys=[]):
		super(MessageBox, self).__init__(vim,
			DropdownForm.OpenNew(open_where, height, title),
			DropdownForm.NormalForm(),
			DropdownForm.TextContent(message),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, *close_keys))

