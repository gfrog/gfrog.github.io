status: published
comments: true
date: 2007-04-04 02:21:38
layout: post
slug: thought-about-net-bank
title: 我也说说网银
wordpress_id: 208
category: Misc

偶是比较后知后觉的那种人,今天才看到python-chinese邮件列表里看到有人说起
[老徐的那封公开信](http://www.billxu.com/friend/rms/an.open.letter.to.cmb.html)
.google了一下,原来几个月以前各大媒体网站原来都报道过这封信.
老徐在公开信里面讲的那个宾馆里的故事实在是很搞笑,
但是偶不知道activex到底在网上银行交易里面扮演一个什么样的角色,
难道就这么不可或缺么?

于是我继续google,似乎activex只是用来防止密码被键盘钩子截获.
似乎这只是对windows系统来说的?

对于非win系统,还有这个问题么?偶不清楚,google也没有找到答案.
但是,activex对于windows就是安全的么? 似乎也不是,看看最近的
[支付宝的activex控件缺陷](http://www.cnbeta.com/modules.php?name=News&file=article&mode=flat&sid=22289)
,看来activex反倒给系统留下了隐患.

看到很多人说国外银行的网银都不用activex的,偶继续google之.

似乎国外银行用的也跟我天朝银行是一样的东西嘛,
除了activex.128位SSL加密,数字证书,usb-key.无非也就是这些了.

但是为啥洋人银行都不用activex呢?
大概洋人都穷,买不起windows,又不像我天朝人手一个盗版windows.
于是activex没了生长的土壤,自己也就躲一边去了.
写到这里不由得感叹我天朝昌盛,连微软都要另眼相看,
每次在天朝卖的windows都比在洋人那里卖的贵.

扯得远了,嘿嘿.
至于这个why activex or why not activex的问题,现在还没有结果.
网友的力量能大过银行么? 也很难说.


这次google过程,也发现了很多有趣的东东,最有意思的莫过于下面这封信了

在Mozine论坛上
[有人帖了一个北京银行客服的回信](http://forums.mozine.cn/index.php?showtopic=14478&st=0&p=79094&#entry79094)
,搞笑之极.实在怀疑写这封信的那位客服人员连什么是网页都不知道.

引用一段,如下:


> 您好，感谢您一直使用并支持北京银行个人网银系统，个人网银新版上线后，我们将不再支持Firefox浏览器，原因如下：
>
> 1、Firefox作为一种开源的浏览器，要求开发的语言必须具有通用性，
>    虽然firefox可以添加许多安全插件，但由于一些插件是第三方开发的，
>    所以语言的差异性就更加的显著，很有可能造成浏览时出现问题。
>
> 2、Firefox为了兼容windows，linux，unix和max os，必须制作一种统一的浏览器内核，
>    而实际上，这些操作系统的网页浏览方式是不一样的，
>    所以在css，javascript，vbscript等网页脚本语言的调用方式上也是不同的，
>    因此，在用非IE的浏览器上使用网上银行会出现样式错乱或者使用出错的情况。
>
> 3、原来的网银系统使用的框架主要是静态jsp实现方式，仅仅应用了很少的样式结构，
>    所以，对于浏览器的兼容性基本没有影响。
>    但是新的网银系统使用了较多的css和较高版本的js，
>    所以会出现对于firefox不兼容的问题。
>
> 鉴于上述原因，我们建议你使用系统自带的IE浏览器，由此给您带来的不便，敬请谅解，
> 在中国传统的春节到来之际，北京银行祝您工作顺利，节日快乐，
> 希望您能一如既往的支持北京银行。谢谢！　



有人回帖说这封信也就是标点用的还没有错误,还算比较贴切,呵呵.

ps.最后搜了一下linux下的键盘记录器,似乎只有到内核里面才能做这件事情,
但是加载驱动之类的操作都是root才能干的,
而linux的使用哲学就是强烈不建议使用root账户作为日常工作账户
(ubuntu甚至干脆不给用户root账号的密码),
这跟在windows里面没有管理员权限就寸步难行有很大的不同.

