status: published
comments: true
date: 2007-04-20 21:47:43
layout: post
slug: interview-questions
title: 都来答答这些问题吧
wordpress_id: 216
category: Misc

细看起来,似乎这些东西都见过.细说起来,这些东西哪个都说不明白是啥.看似能说清楚的,写起来又发现自己还是说不明白.唉,自己这半吊子水平....

来自[baozi的blog](http://blog.xfocus.net/index.php?blogId=3)

1. 线程和进程有什么区别
1. pptp和pppoe有什么区别
1. md5是什么算法
1. apache1和apache2有什么区别
1. 电子签名怎么工作
1. 什么是jail
1. spantree协议说说
1. 列举加密算法，并且分类
1. 什么是正则表达式，用一个 shell检测一个文件是否是c写的
1. 邮件系统的认证方法？说一下邮件系统的证书认证。
1. 交换机和路由器的区别

青蛙自己感觉能说的清楚的只有3,6,7,11.

3: md5是散列算法,或者叫摘要算法.具体咋回事,偶不知道 - -b

6: jail 一个跟系统相对隔离的环境,
   用于安全执行一些特定的服务或者建立蜜罐.
   第一次接触jail这个概念还是在baozi大哥在linuxsir上发的几个帖子里面.
   从那以后一直试图自己建立jail,但是一直未遂.

7: spaningtree 生成树协议,用于消除第二层设备产生的环路.
   这个协议是偶当年在校园网里抓包发现的第一个比较特殊的协议(相对于arp ip tcp来说...)

11: 交换机 二层设备,根据mac-端口对应表工作
   路由器 三层设备,根据ip-端口对应表工作

