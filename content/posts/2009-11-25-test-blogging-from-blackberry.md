status: published
comments: true
date: 2009-11-25 04:40:28
layout: post
slug: test-blogging-from-blackberry
title: 测试黑莓手机发博
wordpress_id: 356
category: Site
tags: blackberry, blog, site, wordpress, client

虽然青蛙的黑莓上早就安装了wordpress客户端，但是它对中文的支持真是一塌糊涂，所以青蛙一直也没用。

再后来，这个客户端的官方网站被封，没办法升级，青蛙就把这个客户端扔到一边去了。
今天无意中找到一个国内提供OTA安装的网站。
赶快升级试用。这不，这个可爱的客户端已经完美支持中文了。

**update:** 2009-11-24

青蛙试用完黑莓版本的wordpress客户端以后，
又试验了一下Android上的WP客户端，用起来也不错，速度很快。
但是没有BB上的功能全面，只能编辑blog，没有处理评论和page的能力。
看来BB用户还是很有福的。

**update:** 2009-11-25

在live writer里面，直接在标题后面加入@@固定链接，
WP就可以将我发布的blog设置为我指定的固定链接了。
但是BB客户端么有这么做。具体原因，需要调查一下。 

发现问题在哪里了，前几天青蛙给WP的插件做了一次大规模升级，
其中就包括了从标题读取slug的插件wp-slug，
这个东东的1.5版会一直试图用google翻译我的标题，
导致我自己设置的slug无法生效。解决方法很简单，给它降级到1.4. ：P