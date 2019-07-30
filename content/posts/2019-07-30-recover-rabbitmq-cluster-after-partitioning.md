Title: 从分区（partitioning）中恢复 RabbitMQ 集群
Date: 2019-07-30 21:36:08
Modified: 2019-07-30 21:36:08
Category: Cloud
Tags: cloud, rabbitmq, cluster, recover, partition, juju
Slug: recover-rabbitmq-cluster-after-partitioning
Authors: gfrog
Status: published
comments: true
layout: post
cover_image: https://miro.medium.com/max/1200/1*UnYL-2r54_7AnEwQv0cVxA.png
Summary: _（本文为 <https://gist.github.com/niedbalski/69a72103adad4f0f9609a0857c9810a4> 的翻译文档。）_


_（本文为
<https://gist.github.com/niedbalski/69a72103adad4f0f9609a0857c9810a4>
的翻译文档。
）_

1) 检查 Cluster 状态。

```bash
Mnesia('rabbit@juju-machine-30-lxd-11'): ** ERROR ** mnesia_event got {inconsistent_database, running_partitioned_network, 'rabbit@juju-machine-29-lxd-9'}

$ sudo rabbitmqctl cluster_status
```

2) 选择合适的节点作为 master 节点。

_（注：这个步骤很重要，如果没有选择合适的 master 节点，很容易造成消息丢失）_

\# 通过连接数。

```bash
$ juju run --service rabbitmq-server "sudo ss -t state established -nt '( sport = :amqp )' | wc -l"
```


\# 最新的 mnesia。

```bash
$ juju run --service rabbitmq-server 'sudo find /var/lib/rabbitmq/mnesia -type f | xargs ls -ltr | tail -n 1 | cut -d " " -f13 | xargs -I {} stat -c "%y" {}'
```

\# Openstack 队列中包含最多的消息数。

```bash
$ juju run --service rabbitmq-server "sudo rabbitmqctl list_queues -p openstack messages | awk '{s+=\$1}END{print s}'"
```


3) 在非 master 节点上停止所有的 epmd/erl 进程。

```bash
$ /etc/init/rabbitmq-server stop
$ sudo killall epmd
```

_（注：在 juju 的环境里还需要关掉 jujud 以免 juju 自作主张重启 rabbitmq server）_

```bash
$ sudo systemctl stop jujud-unit-rabbitmq-server-0.service
```

确认所有的 rabbitmq 进程都被杀掉了：

```bash
$ sudo ps -U rabbitmq -o pid --no-heading
```

4) 删除 mnesia，重新启动 rabbitmq 服务，然后停止 app。

```bash
$ sudo mv /var/lib/rabbitmq/mnesia /var/lib/rabbitmq/mnesia-back
$ sudo service rabbitmq-server start
$ sudo rabbitmqctl stop_app
```

确认 rabbitmq 服务启动，并且未加入 cluster。 (`$ sudo rabbitmqctl cluster_status`)

5) 在 master 节点上忘记（forget） 其他节点。

```bash
$ sudo rabbitmqctl stop_app
$ sudo rabbitmqctl forget_cluster_node rabbit@trashed-slave
$ sudo rabbitmqctl start_app
```


_（注：这里应该有比较重要的一步，就是检查所有节点上的 `cluster_name`。
一定要确保其他节点上的`cluster_name`跟 master 节点一致。所以青蛙把这一步作为5.1）_

5.1) 检查并确认 `cluster_name`。

```bash
$ juju run --application rabbitmq-server "sudo rabbitmqctl cluster_status |grep cluster_name"
```

如果 `cluster_name` 不一致，需要在其他节点上修改 `cluster_name`：

```bash
$ sudo rabbitmqctl set_cluster_name rabbit@juju-machine-29-lxd-9
```

6) 将节点加入 cluster，在要加入的节点上执行：

```bash
$ sudo rabbitmqctl join_cluster rabbit@master
$ sudo rabbitmqctl start_app
```

7) 检查 clutser 状态。

```bash
$ juju run --application rabbitmq-server "sudo rabbitmqctl cluster_status"
```

8) 建议将 rabbitmq-server charm 的 `cluster-partitioning-handling` 选项设置为 `autoheal`。

_（注：这里需要注意`autoheal`可能会使 rabbitmq 丢失数据，所以也应该谨慎使用过。）_

<https://github.com/openstack/charm-rabbitmq-server/blob/master/config.yaml#L39>


**Update:**

关于 rabbitmq 基本内容，以及 partition 和 brain split 的一个介绍。

* 关于RabbitMq你必须深入理解的内容 <https://zhuanlan.zhihu.com/p/60141062>
