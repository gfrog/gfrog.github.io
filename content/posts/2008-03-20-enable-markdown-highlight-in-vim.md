status: published
comments: true
date: 2008-03-20 00:29:34
layout: post
slug: enable-markdown-highlight-in-vim
title: 在VIM中打开Markdown文件高亮
wordpress_id: 302
category: VIM
tags: VIM, Markdown, configuration, vimrc

[Markdown](http://daringfireball.net/projects/Markdown/)
是John Gruber设计的一个文本标记系统，相比html，它很简单，
便于手工编写，而且它还支持
[Wordpress](http://wordpress.org/)
，
[有一个用于wordpress的插件](http://michelf.com/projects/php-Markdown/)
。青蛙决定用vim+Markdown来编写blog，看起来他们是一对强大的组合 :)

首先要去
[Vim](http://www.vim.org/)
的官方网站
[下载Markdown的语法高亮插件](http://www.vim.org/scripts/script.php?script_id=1242)
，并把它复制到"~/.vim/syntax/"目录下面。
然后，新建一个"~/.vim/ftdetect/mkd.vim"文件，在其中加入下面的内容：

```vimrc
" markdown filetype file
if exists("did_load_filetypes")
  finish
endif
augroup markdown
  au! BufRead,BufNewFile *.mkd   setfiletype mkd
augroup END
```

并在"~/.vimrc"文件中添加如下内容：

```vimrc
"Markdown language syntax settings
augroup mkd
  autocmd BufRead *.mkd  set ai formatoptions=tcroqn2 comments=n:>
augroup END
```

然后，后缀名为".mkd"的文件就能被自动启用Markdown的语法高亮了。
