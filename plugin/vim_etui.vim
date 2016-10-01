" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python sys.path.append(vim.eval('expand("<sfile>:h")')+'/widgets')
python sys.path.append(vim.eval('expand("<sfile>:h")')+'/widgets/libs')

python << endOfPython
import vim
from vim_extend  import VimExtend

import message_box
import list_menu
import rich_message_box
import dropdown_form
import stateful_object
import extended_lock

class VimETUI(object):
	DropdownForm = rich_message_box.DropdownForm
	StatefulObject = stateful_object.StatefulObject
	Lock = extended_lock.Lock

	class MessageBox(message_box.MessageBox):
		DEFAULT_EXIT_KEYS = ['<CR>', '<C-C>']
		DEFAULT_HEIGHT = 15
		def __init__(self, **options):
			options.setdefault('message', '')
			options.setdefault('title', '')
			options.setdefault('height', VimETUI.MessageBox.DEFAULT_HEIGHT)
			options.setdefault('open_where', VimETUI.DropdownForm.Position.Bottom)
			options.setdefault('close_keys', VimETUI.MessageBox.DEFAULT_EXIT_KEYS)
			super(VimETUI.MessageBox, self).__init__(VimETUI.vim(), **options)

	class ListMenu(list_menu.ListMenu):
		DEFAULT_EXIT_KEYS = ['<C-C>']
		DEFAULT_HEIGHT = 15
		def __init__(self, **options):
			options.setdefault('lines', [])
			options.setdefault('colors', [])
			options.setdefault('title', '')
			options.setdefault('height', VimETUI.ListMenu.DEFAULT_HEIGHT)
			options.setdefault('open_where', VimETUI.DropdownForm.Position.Bottom)
			options.setdefault('keys', [])
			options.setdefault('export_model', 'VimETUI')
			options.setdefault('close_keys', VimETUI.ListMenu.DEFAULT_EXIT_KEYS)
			super(VimETUI.ListMenu, self).__init__(VimETUI.vim(), **options)

	class RichMessageBox(rich_message_box.RichMessageBox):
		DEFAULT_HEIGHT = 15
		def __init__(self, **options):
			options.setdefault('title', '')
			options.setdefault('height', VimETUI.ListMenu.DEFAULT_HEIGHT)
			options.setdefault('open_where', VimETUI.DropdownForm.Position.Bottom)
			super(VimETUI.RichMessageBox, self).__init__(VimETUI.vim(), **options)

	@staticmethod
	def vim():
		return VimExtend.extend(vim)

endOfPython








"================================================================================
" TEST ing
function! EUIListMenu(title, lines, colors, keys, handler_name)
python << endOfPython

def test_show(key):
	print key
	print VimETUI.vim().current_cursor()

VimETUI.ListMenu(title=vim.eval('a:title'), lines=vim.eval('a:lines'), colors=vim.eval('a:colors'), keys=vim.eval('a:keys'), handler=test_show).show()

endOfPython
endfunction
function! TestListMenu()
	call EUIListMenu('Hello', [['A', 'B'], ['00', '01'], ['aoeuoeau']], ['green', 'yellow'], ['e'], 'Print_key_line')
endfunction

command! -nargs=* ETestLM call TestListMenu(<f-args>)

function! TestRichBox(file)
python << endOfPython

rich_message_box = VimETUI.RichMessageBox(title='Test')
rich_message_box.show()
with open(vim.eval('a:file')) as f:
    for line in f:
		rich_message_box.append([line])

endOfPython
endfunction
