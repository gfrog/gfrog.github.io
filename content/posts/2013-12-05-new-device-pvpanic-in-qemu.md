status: published
comments: true
layout: post
title: QEMU中的 pvpanic设备
date: 2013-12-05 17:27:19 +0800
category: Virt
tags: virt, qemu, command, shell, device

pvpanic设备是在Qemu-1.5的时候引入的一个ISA设备\[1\]，
旨在让hypervisor可以感知guest kernel panic，并作出相应的处理。
在目前的实现中，pvpanic使用了一个固定的I/O端口（默认为0x505），
向这个端口的bit 0写入1的时候，即意味着guest kernel panic发生了。


首先，先来玩一玩这个设备，看看它到底会干点啥。

青蛙目前用的Ubuntu Saucy 系统上面的 Qemu 版本是1.6.0。
由于pvpanic设备在设计过程中并没有过多的考虑windows guest的情况，
并且libvirt支持这个设备也遇到了困难，所以qemu的开发者们曾经就这个设备发生了一大串的讨论\[2\]。
所以在现在的Qemu 1.7.\*, 1.6.\*, 1.5.4+中，这个功能都是默认关闭的，
要使用这个pvpanic，还需要几条额外的选项：

```bash
qemu-system-x86_64 -name test-pvpanic -nodefaults -cpu host -m 1024 -M pc \
-smp 1,sockets=1,cores=1,threads=1 \
-chardev socket,id=charmonitor,path=/tmp/monitor-test-pvpanic.sock,server,nowait \
-mon chardev=charmonitor,id=monitor,mode=control \
-drive file=test-pvpanic.qcow2,if=none,id=drive-virtio-disk0,format=qcow2 \
-device virtio-blk-pci,scsi=off,bus=pci.0,addr=0x5,drive=drive-virtio-disk0,id=virtio-disk0 \
-vnc :0 \
-device cirrus-vga,id=video0,bus=pci.0,addr=0x2 \
-
```


**Links**

\[1\] https://github.com/qemu/qemu/blob/master/docs/specs/pvpanic.txt

\[2\] pvpanic plans?[http://thread.gmane.org/gmane.comp.emulators.qemu/229289](http://thread.gmane.org/gmane.comp.emulators.qemu/229289)
