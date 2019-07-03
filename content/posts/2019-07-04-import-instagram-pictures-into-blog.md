title: 将Instagram内容导入Blog
date: 2019-07-04 00:07:46
slug: import-instagram-pictures-into-blog
category: Site
comments: true
layout: post
status: published
tags: site, instagram, python
cover_image: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1200px-Instagram_logo.svg.png
cover_image_by: Instagram
cover_image_link: http://instagram.com/
Summary: 青蛙关站的这几年，虽然没有写blog，但是instagram和twitter发了可真不少。今天研究了下怎么导入instagram的照片和twitter的条目。看起来instagram很容易实现，因为有一个python的客户端Instaloader。

青蛙关站的这几年，虽然没有写blog，但是instagram和twitter发了可真不少。
今天研究了下怎么导入instagram的照片和twitter的条目。
看起来instagram很容易实现，因为有一个python的客户端
[Instaloader](https://instaloader.github.io/)
。

首先，用pip把这个客户端装上
```
$ pip3 install instaloader
```

然后，自己搞个脚本，从instagram数据里面直接生成markdown文件，写的不太好看，不过数据基本完美导入Blog了。





[gist:id=92087c750e9293213b69f0f1765e3fad]

目前没有解决的问题有两个，这两点以后有时间再研究吧。

* 如果有新的instagram内容，可能需要有一个daemon每天监测然后转换成markdown。
* <del>没办法处理视频内容，现在只是把视频文件链接留下了，但是没办法直接在blog播放。
  之后有时间需要找一个嵌入video的办法。
  **Update:** 原来liquid_tags.video插件就可以插入video，只需要在post里写
  `{ % video link width height % }`
  就好了。</del>
  **Update 2:** Instagram 的 video link 几天之后就失效了。
  所以目前青蛙的办法是直接在 Instram 里面导出 video 的 embed code，贴到 post 里面就好。


