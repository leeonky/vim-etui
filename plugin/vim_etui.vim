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

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! -nargs=* EUIMessage call EUIMessage(<f-args>)
