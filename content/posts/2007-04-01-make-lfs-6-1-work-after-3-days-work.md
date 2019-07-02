status: published
comments: true
date: 2007-04-01 13:13:39
layout: post
slug: make-lfs-6-1-work-after-3-days-work
title: 奋斗三天 LFS终于成功
wordpress_id: 206
category: Linux
tags: lfs, linux

从前天晚上开始做lfs-6.1,到今天上午12点,终于启动到了lfs系统下面.

先恭喜自己一下.呼呼.

这次lfs不是那么完美的,因为最后一步编译的内核没有起来.
估计是没有initrd的原因.但是说到底还是我的内核配置有问题.
我直接把宿主系统上的2.6.18内核抓来用了.嘿嘿,这还是算是lfs的吧...

秀几个图吧.

先是grub:

[![grub.jpg](http://gfrog.cn/attachments/month_0704/x200741131246.jpg)](http://gfrog.cn/attachments/month_0704/x200741131246.jpg)

然后是启动起来,login的界面: (嗯,我把这个系统命名为gLinux0.02 哈哈 大家还记得gLinux0.01吧 -_-)

[![login.jpg](http://gfrog.cn/attachments/month_0704/y200741131320.jpg)](http://gfrog.cn/attachments/month_0704/4200741131311.jpg)

然后是uname -a: lfs-6.1默认的是2.6.11.2内核,但是我编译的起不来,现在看到的是debian的2.6.18内核.

以后偶再也不敢说编译内核简单了,最近10次编译内核全部以失败告终,泪...

[![uname.jpg](http://gfrog.cn/attachments/month_0704/o200741131338.jpg)](http://gfrog.cn/attachments/month_0704/p200741131331.jpg)

最后是lfs ID的截图:

[![lfsID.jpg](http://gfrog.cn/attachments/month_0704/5200741131251.jpg)](http://gfrog.cn/attachments/month_0704/y200741131248.jpg)

列一下我的参考资料吧.这次做lfs偶换掉了几个6.1默认的包,用了6.1.1或者6.2中的包.所以从6.1的手册到6.2的手册都看了一些.下面是6.1跟6.1.1的中文版.

6.1中文:　[http://lfs.linuxsir.org/doc/lfs6.1zh/index.html](http://lfs.linuxsir.org/doc/lfs6.1zh/index.html)

6.1.1中文: [http://www.dogdoghome.com/lamp/Linux/LFS-6.1.1/index.html](http://www.dogdoghome.com/lamp/Linux/LFS-6.1.1/index.html)

6.2英文: [http://www.linuxfromscratch.org/lfs/view/stable/index.html](http://www.linuxfromscratch.org/lfs/view/stable/index.html)

还有就是linuxsir上
[大牛youbest的文章](http://www.linuxsir.org/bbs/showthread.php?t=244052)
,我基本上是照这里作的,真是太方便了,真诚感谢这样的大牛的付出.

最后,要说lfs-6.1里面的一个bug,
就是Tcl-8.4.9的configure脚本有一个错误,
cofigure的时候过不去.要用下面的命令修改它的configure脚本:

```
<kbd>sed -i "s/relid'/relid/" configure</kbd>
```

这个错误在lfs-6.1.1里面改正了.如果还在用lfs-6.1的手册,那么就要注意这点了.

Del.icio.us : [linux lfs](http://del.icio.us/tag/linux+lfs)



