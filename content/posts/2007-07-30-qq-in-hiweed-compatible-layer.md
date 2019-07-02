status: published
comments: true
date: 2007-07-30 22:34:23
layout: post
slug: qq-in-hiweed-compatible-layer
title: 传说中的QQ,传说中的hiweed兼容层
wordpress_id: 263
category: Linux
tags: Hiweed, Linux, QQ

今天有人在irc上说起了QQ,大家七嘴八舌议论现在linux的各路QQ客户端.
Shely老大给了
[ubuntu.org.cn上面的一个帖子](http://forum.ubuntu.org.cn/about63843.html)
.偶照着上头做了下,真的搞定了QQ.

以下为引用:


> 先执行下代码: <br />
> sudo sed -ie '/GBK/,/^}/d' /usr/share/X11/locale/zh_CN.UTF-8/XLC_LOCALE <br />
> 然后下载 <br />
> http://linuxfire.com.cn/~huahua/zero/qq2007beta1kb5_0.0.2007_x86.tgz <br />
> http://211.92.88.40/~huahua/zero/qq2007beta1kb5_0.0.2007_x86.tgz <br />
> ( 或者 qq2007beta1kb5_0.0.2007_x6.tgz: http://files.filefront.com//;8150970;;/ ) <br />
> 解压，执行里边的 qq2007beta1kb5 <br />
> 就打开 qq 了 <br />
> ------------------ <br />
> 如果您的 scim 在里边不上字的话，请在 scim 首选项-》全局设置 里 去掉 “将预编辑字符串嵌入到客户窗口中”

经过我一天的试用,QQ运行状态良好.为了QQ客户端郁闷的各位,有这个方法好了.
