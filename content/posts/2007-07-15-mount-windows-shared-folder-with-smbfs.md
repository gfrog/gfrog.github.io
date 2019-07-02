status: published
comments: true
date: 2007-07-15 08:48:06
layout: post
slug: mount-windows-shared-folder-with-smbfs
title: 关于linux下访问windows共享的问题
wordpress_id: 260
category: Linux
tags: Linux, Samba, Shared, Windows

首先，需要安装smbfs包

```
# aptitude install smbfs
```

如果没有安装这个包,挂载共享分区时会出现以下错误

> smbfs: mount_data version 1919251317 is not supported.

然后,挂载windows共享的命令是

```
mount  -t smbfs //ip/共享名 -o username=用户名,password=密码,iocharset=utf-8,dmask=777,fmask=777 /media/smb
```

说下参数,

> ip,共享名,就是要访问的windows共享资源了 <br />
> 用户名,密码,是在那个windows系统上的用户名密码. <br />
> dmask=777,fmask=777, 共享分区的读写权限,这里设成777了.根据自己需要改吧. <br />
> /media/smb ,共享分区挂载的本地路径.

/etc/fstab的写法,在/etc/fstab里面添加如下一行:

```
//ip/共享名 /media/smbf smbfs defaults,username=用户名,password=密码,iocharset=utf-8,dmask=777,fmask=777     0       1
```

参数意义跟用mount命令时一样.

最后,google到网上有些地方写了smbmount命令,
这个命令不知道是哪个发行版里面带的,
至少在debian里面现在没有了(现在指的是debian lenny版本),
挂载共享直接mount然后指定smbfs格式就行.

ps.如果只是想在x里面查看windows共享,
只要在nautilus里面文件->连接到服务器里面,连接到一个windows共享就行了.

参考文章:

1.[一步一学Linux与Windows 共享文件Samba （v0.2b）](http://www.linuxsir.org/main/?q=node/158)

2.[Mounting remote filesystems with smbfs](http://gfrog.net/wp-admin/Mounting%20remote%20filesystems%20with%20smbfs)(英文)
