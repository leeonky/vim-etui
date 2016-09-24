" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python sys.path.append(vim.eval('expand("<sfile>:h")')+'/widgets')

python << endOfPython
import vim
from vim_extend  import VimExtend

import message_box
import list_menu
import rich_message_box
import dropdown_form

class ETUI(object):
	DropdownForm = rich_message_box.DropdownForm
	class MessageBox(message_box.MessageBox):
		DEFAULT_EXIT_KEYS = ['<CR>', '<C-C>']
		DEFAULT_HEIGHT = 15
		def __init__(self, **options):
			options.setdefault('message', '')
			options.setdefault('title', '')
			options.setdefault('height', ETUI.MessageBox.DEFAULT_HEIGHT)
			options.setdefault('open_where', ETUI.DropdownForm.Position.Bottom)
			options.setdefault('close_keys', ETUI.MessageBox.DEFAULT_EXIT_KEYS)
			super(ETUI.MessageBox, self).__init__(ETUI.vim(), **options)

	class ListMenu(list_menu.ListMenu):
		DEFAULT_EXIT_KEYS = ['<C-C>']
		DEFAULT_HEIGHT = 15
		def __init__(self, **options):
			options.setdefault('lines', [])
			options.setdefault('colors', [])
			options.setdefault('title', '')
			options.setdefault('height', ETUI.ListMenu.DEFAULT_HEIGHT)
			options.setdefault('open_where', ETUI.DropdownForm.Position.Bottom)
			options.setdefault('keys', [])
			options.setdefault('handler_name', '')
			options.setdefault('close_keys', ETUI.ListMenu.DEFAULT_EXIT_KEYS)
			super(ETUI.ListMenu, self).__init__(ETUI.vim(), **options)

	@staticmethod
	def vim():
		return VimExtend.extend(vim)

endOfPython

" --------------------------------
" ListMenu
" --------------------------------
function! EUIListMenu(title, lines, colors, keys, handler_name)
python << endOfPython

ETUI.ListMenu(title=vim.eval('a:title'), lines=vim.eval('a:lines'), colors=vim.eval('a:colors'), keys=vim.eval('a:keys'), handler_name=vim.eval('a:handler_name')).show()

endOfPython
endfunction

function! EUIClickableLineHandeler(key, handler_name)
	let Handler = function(a:handler_name)
	call call(Handler, [a:key, getline('.')])
endfunction

"================================================================================
" TEST ing
function! TestListMenu()
	call EUIListMenu('Hello', [['A', 'B'], ['00', '01'], ['aoeuoeau']], ['green', 'yellow'], ['e'], 'Print_key_line')
endfunction

function! Print_key_line(key, line)
	echo a:key
	echo a:line
endfunction

command! -nargs=* ETestLM call TestListMenu(<f-args>)

function! TestRichBox(file)
python << endOfPython
import vim
from vim_extend  import VimExtend
from rich_message_box import RichMessageBox

rich_message_box = RichMessageBox(VimExtend.extend(vim), title='Test')
rich_message_box.show()
with open(vim.eval('a:file')) as f:
    for line in f:
		rich_message_box.append_rich(line)

endOfPython
endfunction
