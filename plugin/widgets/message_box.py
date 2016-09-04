from dropdown_form import DropdownForm

class MessageBox(DropdownForm):
	def __init__(self, vim, title='', message='', height=10):
		super(MessageBox, self).__init__(vim,
			DropdownForm.OpenNew(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.TextContent(message),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, '<CR>', '<C-C>'))

