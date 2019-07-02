status: published
comments: true
date: 2007-07-16 19:33:56
layout: post
slug: linux-usb-mod-conflict
title: 郁闷了2天的U盘问题,竟然是因为内核模块
wordpress_id: 262
category: Linux
tags: Debian, Linux, Storage, USB

真的真的被debian打败了,U盘插到机器上以后,死活就是认不出来,dmesg上面有消息说插上了,但是是下面这样的消息:


> Initializing USB Mass Storage driver... <br />
> usbcore: registered new interface driver usb-storage <br />
> USB Mass Storage support registered. <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 7 <br />
> ehci_hcd 0000:00:1d.7: port 4 reset error -110 <br />
> hub 4-0:1.0: hub_port_status failed (err = -32) <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 11 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 15 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 18 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 22 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 29 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 33 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 40 <br />
> ehci_hcd 0000:00:1d.7: port 4 reset error -110 <br />
> hub 4-0:1.0: hub_port_status failed (err = -32) <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 59 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 73 <br />
> usb 4-4: new high speed USB device using ehci_hcd and address 80 <br />
> ehci_hcd 0000:00:1d.7: port 4 reset error -110 <br />
> hub 4-0:1.0: hub_port_status failed (err = -32)

然后lsusb根本没有反应.
于是从昨天开始就在找这个原因,
因为以前装的很多debian系统根本没这个问题,
无论是sarge还是etch.

结果这次升级到lenny就出了这么个状况.

开始走了一个很大的弯路,
因为google到有人说这个问题可能是acpi问题引起的,
我想也有可能,因为这个机器是个T40的本子.
于是想连acpi一起配好吧,于是acpid,cpufreqd一顿研究,
问题还是没好,U盘插上灯连亮都不给我亮一下.

结果今晚忽然想起来我还没搜过这个错误提示呢,
结果按上面ehci_hcd的错误提示一搜,
马上就有了结果(在
[这里](http://moto.debian.org.tw/viewtopic.php?t=4932)
).原来挂不上U盘的原因是模块造成的.
以前就听说过这几个usb模块打架,今天就让我碰上了.

问题知道了,解决方法也很简单,root模式下执行:

```
# rmmod ehci_hcd
```

然后插上U盘,盘上可爱的小绿灯又亮起来了,真开心.
