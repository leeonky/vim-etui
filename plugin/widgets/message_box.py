from dropdown_form import DropdownForm

class MessageBox(DropdownForm):
	def __init__(self, vim, message='', title='', height=10, open_style=None):
		super(MessageBox, self).__init__(vim,
			open_style or DropdownForm.OpenNew(DropdownForm.Position.Bottom, 10, title),
			DropdownForm.NormalForm(),
			DropdownForm.TextContent(message),
			DropdownForm.DisableEdit(),
			DropdownForm.CloseAndFocusBack(vim.current.window.number, *vim.vars['message_box_exit_key']))

