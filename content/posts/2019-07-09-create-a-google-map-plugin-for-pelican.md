Title: Pelican 的 Google Map 插件
Date: 2019-07-09 14:27:10
Modified: 2019-07-09 14:27:10
Category: Site
Tags: pelican, google, map, python, script, coding, github
Slug: create-a-google-map-plugin-for-pelican
Authors: gfrog
status: published
comments: true
layout: post
cover_image: http://pluspng.com/img-png/google-maps-png-open-2000.png
cover_image_by: pluspng.com
cover_image_link: http://pluspng.com/google-maps-png-1570.html
Summary: 青蛙最近整理照片和blog的时候，一直想想在blog post里添加一个地图。 但是pelican似乎没有靠谱的google map plugin。 虽然有一个google_embed，但是似乎现在不能用了，按照它的README写好map之后，post里面完全不会转义。 于是青蛙一怒之下自己照猫画虎写了个liquid_tag版本的google map，竟然也能用了。


青蛙最近整理照片和blog的时候，一直想想在blog post里添加一个地图。
但是pelican似乎没有靠谱的google map plugin。
虽然有一个
[google_embed](https://pypi.org/project/google_embed/)
，但是似乎现在不能用了，按照它的README写好map之后，post里面完全不会转义。

于是青蛙一怒之下自己照猫画虎写了个liquid_tag版本的google map，竟然也能用了。

目前这个plugin支持map和direction模式，青蛙还在考虑要不要添加街景模式。

添加map的方法：
```php
    {% gmap "location" mode [maptype] [align] [width] [height] %}
```
`location`：必选项，指定地点，必须包含双引号，支持中文。

`mode`：必选项，地图模式，有`place`和`search`选项，
指定地图显示单个地点或者搜索location中的关键字

`maptype`：地图的显示模式，包含`roadmap`、`satellite`、`hybrid`和`terrain`。

`align`：地图在页面中的对齐方式，`left`、`center`或者`right`

`width`：地图宽度

`height`：地图高度

例如： `{ % gmap "东方明珠,上海" place roadmap left 600 480 % }` 显示如下地图：

{% gmap "东方明珠,上海" place roadmap left 600 480 %}



添加direction（导航）的方法：
```php
    {% gdirection "origin" "destination" ["waypoints"] mode [maptype] [align] [width] [height] %}
```
`origin`：必选项，指定出发点，必须包含双引号，支持中文。

`destination`：必选项，指定目的地，必须包含双引号，支持中文。

`waypoints`：指定途经点，必须包含双引号，支持中文。

`mode`：必选项，导航模式，有`driving`、`walking`、`bicycling`、
`transit`和`flying`选项。

`maptype`：地图的显示模式，包含`roadmap`、`satellite`、`hybrid`和`terrain`。

`align`：地图在页面中的对齐方式，`left`、`center`或者`right`。

`width`：地图宽度。

`height`：地图高度。

例如： `{ % gdirection "东方明珠,上海" "人民广场,上海" driving roadmap left 600 480 % }` 显示如下地图：

{% gdirection "东方明珠,上海" "人民广场,上海" driving roadmap left 600 480 %}

如果你也想在pelican里面使用这个插件，可以在
[Google cloud plateform console](https://console.cloud.google.com/projectselector2/google/maps-apis/api-list?supportedpurview=project&project&folder&organizationId)
申请一个MAP API key，然后在`pelicanconfig.py`文件里加入API key配置：
```python
GMAPS_API_KEY = "YOUR_API_KEY_HERE"
```

然后给liquid_tag打个补丁：

[gist:id=a13b27768172f40d20632cadd8614061,file=gmap.diff]

接着把这个文件放进liquid_tags目录里面，然后就可以在post里添加地图了。

Enjoy posting!

[gist:id=a13b27768172f40d20632cadd8614061,file=gmap.py]


参考文档：

\[1\] [Google Embed](http://iza.ac/posts/2014/03/google-embed/)

\[2\] [google_embed](https://pypi.org/project/google_embed/)

\[3\] [Liquid-style Tags](https://github.com/getpelican/pelican-plugins/blob/master/liquid_tags/Readme.md)



