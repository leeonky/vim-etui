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
function! TemplateExample()
python << endOfPython
import vim

from message_box import MessageBox

MessageBox(vim, 'Hello you', 'World').show()

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! Example call TemplateExample()
