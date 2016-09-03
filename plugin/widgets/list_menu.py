from dropdown_form import DropdownForm

class ListMenu(DropdownForm):
	def __init__(self, vim, title, height):
		super(ListMenu, self).__init__(vim,
			DropdownForm.OpenShow(DropdownForm.Position.Bottom, 10, title))
