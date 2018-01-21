[comment]: <> (pandoc test.md -o test.docx)
[comment]: <> (the command can generate the .docx file)

第2章 CAN总线网络结构设计及其应用层协议研究
======================================
&emsp;&emsp;网络中各个节点相互联接的方法和形式称为网络拓扑。作为网络上的节点，车辆电子设备具有种类繁多并且信号性质也各不相同的特点。根据节点相互之间的通信关系，确定合适的网络拓扑结构是建立车用网络体系的第一步。合理的网络拓扑结构对于优化网络性能降低网络复杂性、增加可靠性及降低成本是非常重要的。

这是行间公式
$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

$$x=\frac{-\sigma\pm\sqrt{b^2-4ac}}{2a}$$
这里是行内公式 \\(E = mc^2\\) 这里是行内公式

&nbsp;//半角空格（英文）
&emsp;//全角空格（中文）


## 行尾用两个空格表示换行

2.1 前言
-------


&emsp;&emsp;
*CAN*
总线的全称是控制器局域网，英文全称：
**Controller Area Network**,
它是由德国BOSCH公司自行开发的多主控点的串行数据通讯协议，是当今国际上运用最广泛的标准现场总线之一。随着CAN总线技术的发展，其应用领域目前已不再局限于汽车行业，而是向过程工业、机械工业、纺织机械、农用机械、机器人、数控机床、医疗器材及传感器等领域发展。目前国际上一些发达国家，在农机具上主要采用 CAN 总线来进行各个电子控制单元
***（Electronic Control Unit，ECU）***
间的通信[2]。CAN 总线作为农机网络节点连接的标准总线，对传感器、控制部件、执行器、信息存储和显示单元之间的数据传输格式和方法进行了规定，可有效提高农机 各项性能，同时压缩了产品开发周期，降低开发成本[3-4]。


2.2 总线节点建模
-----
1. 网络中各个节点相互联接的方法和形式称为网络拓扑。作为网络上的节点，车辆电子设备具有种类繁多并且信号性质也各不相同的特点。根据节点相互之间的通信关系，确定合适的网络拓扑结构是建立车载网络模型重要的一步。合理的网络拓扑结构对于优化网络性能，降低网络复杂性、增加可靠性及降低成本是非常重要的。车载局域网络有各种各样的拓扑结构，典型的有总线型、环形和星型，如图：
2. 智能农机上的网络特点可归纳为通讯距离短、子功能模块化较好、扩充性要求高、网络复杂度要求不高、可靠性要求高等。因此。考虑智能农机网络的特点将这些拓扑结构进行比较,可以看出总线型的结构是最适合车用网络体系的。
3. 智能农机上的网络特点可归纳为通讯距离短、子功能模块化较好、扩充性要求高、网络复杂度要求不高、可靠性要求高等。因此。考虑智能农机网络的特点将这些拓扑结构进行比较,可以看出总线型的结构是最适合车用网络体系的。

## 图片链接
![](https://i.imgur.com/7xQPeNr.png)

![](https://i.imgur.com/UrNWxVw.png)

![](https://i.imgur.com/CESseSN.png)

![](https://i.imgur.com/l7c3aIW.png)

![](https://i.imgur.com/7u1lDnq.png)

![](https://i.imgur.com/rgZFPXI.png)

![](https://i.imgur.com/ILfKNuf.png)

## 注释
[comment]: <> (This is a comment, it will not be included)
[comment]: <> (in  the output file unless you use it in)
[comment]: <> (a reference style link.)
[//]: <> (This is also a comment.)
[//]: # (This may be the most platform independent comment)

## 相对路径，文件在本地存着
![the picture name](./1.png)

## 生成表格，线框可能是透明的
| name | age | life |
| ---- | :-: | ---: |
| Dean | 23 | live|
| Dean | 23 | live|