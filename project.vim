#! /usr/bin/vim -S
"set expandtab
set shiftwidth=2
set tabstop=2

let g:test_all_test=['/bin/bash', '-c', "python -m unittest discover && lettuce"]
let g:test_current_ut=['python', '-m', 'unittest', 'discover']
let g:test_current_at=['lettuce']
let g:test_bdd_features=['lettuce']
