Title: 修复因为 Python 升级导致的失效 virtualenv 环境
Date: 2019-07-17 20:48:27
Modified: 2019-07-17 20:48:27
Category: Programming
Tags: python, python3, virtualenv, macos, osx, homebrew, shell
Slug: fix-python-virtualenv-after-python-upgrade
Authors: gfrog
Status: published
comments: true
layout: post
cover_image: https://i1.wp.com/www.alexwhittemore.com/wp-content/uploads/2018/08/Untitled-drawing.jpg?ssl=1
cover_image_by: PYTHON ON MACOS: BEST PRACTICES
cover_image_link: https://www.alexwhittemore.com/python-on-macos-best-practices/
Summary: _（本篇日志为How to fix your Python virtualenv after a Homebrew Python upgrade的翻译文档）_

_（标题图片借用
[PYTHON ON MACOS: BEST PRACTICES](https://www.alexwhittemore.com/python-on-macos-best-practices/)
的标题图，这篇文档也是关于MacOS上面运行python和virtualenv的。）_

_（本篇日志为
[How to fix your Python virtualenv after a Homebrew Python upgrade](http://www.jeremycade.com/python/osx/homebrew/2015/03/02/fixing-virtualenv-after-a-python-upgrade/)
的翻译文档）_

你在使用Homebrew管理你的OS X上面的Python嘛？最近有没有升级过Python？

我遇到的情况是Python 3的一个小更新：从3.4.2到3.4.3。
这个升级足够让virtualenv里面的符号连接（symbolic links）失效了。

**例如**
```bash
~: cd ~/src/my_app
~/src/my_app: source venv/bin/activate
[venv] ~/src/my_app: python
dyld: Library not loaded: @executable_path/../.Python
  Referenced from: /Users/jeremycade/src/my_app/env/bin/python
  Reason: image not found
Trace/BPT trap: 5
```

正如我提到的那样，virtualenv内部的符号连接都指向了Homebrew安装的Python，
升级之后这些符号连接都指向了错误的地方。
解决方法是删除然后重建这些符号连接。

首先，我们需要确保你的virtualenv没有生效（active）。
```bash
[venv] ~/src/my_app: deactivate
```

然后，删除这些错误的符号连接。
```bash
~/src/my_app: find venv -type l -delete
```

这里我使用了OS X自带的BSD
[find](http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man1/find.1?query=find)
命令。

最后一步，重建你的virtualenv。
```bash
~src/my_app: virtualenv venv
```

--------

**青蛙注**

青蛙没有详细的研究这个问题。
但是感觉上应该是
[virtualenv](https://virtualenv.pypa.io/)
这个包引入的，如果使用python3内建的venv module，
`python3 -m venv VENV_DIR`
这种方式创建virtualenv的时候，并不会创建符号连接。

所以结论是，在MacOS上尽量使用python内置的venv模块，
而不是使用virtualenv包。
