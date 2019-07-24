
autocmd BufNewFile *.py execute 'silent! 1s:.*:#!/usr/bin/env python3'

if has("autocmd")
  filetype plugin indent on
endif


