" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))
python sys.path.append(vim.eval('expand("<sfile>:h")')+'/widgets')

" --------------------------------
"  Function(s)
" --------------------------------
function! EUIMessage(title, content)
python << endOfPython
import vim

from message_box import MessageBox
from vim_extend  import VimExtend

MessageBox(VimExtend.extend(vim), message=vim.eval('a:content'), title=vim.eval('a:title')).show()

endOfPython
endfunction

function! EUIListMenu(title, lines, colors, keys, handler_name)
python << endOfPython
import vim

from list_menu import ListMenu
from vim_extend  import VimExtend

ListMenu(VimExtend.extend(vim), title=vim.eval('a:title'), lines=vim.eval('a:lines'), colors=vim.eval('a:colors'), keys=vim.eval('a:keys'), handler_name=vim.eval('a:handler_name')).show()

endOfPython
endfunction

function! EUIClickableLineHandeler(key, handler_name)
	let Handler = function(a:handler_name)
	call call(Handler, [a:key, getline('.')])
endfunction

" TEST ing
function! TestListMenu()
	call EUIListMenu('Hello', [['A', 'B'], ['00', '01'], ['aoeuoeau']], ['green', 'yellow'], ['e'], 'Print_key_line')
endfunction

function! Print_key_line(key, line)
	echo a:key
	echo a:line
endfunction

command! -nargs=* ETestLM call TestListMenu(<f-args>)

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! -nargs=* EUIMessage call EUIMessage(<f-args>)
