## 前言

在工作中经常会遇到各种websehll，黑客通常要通过各种方式获取 webshell，从而获得企业网站的控制权，识别出webshell文件或通信流量可以有效地阻止黑客进一步的攻击行为，下面以常见的四款webshell进行分析，对工具连接流量有个基本认识。

## **Webshell****简介**

webshell就是以[asp](https://baike.baidu.com/item/asp/128906)、[php](https://baike.baidu.com/item/php/9337)、jsp或者cgi等[网页](https://baike.baidu.com/item/%E7%BD%91%E9%A1%B5/99347)文件形式存在的一种代码执行环境，主要用于网站管理、服务器管理、权限管理等操作。使用方法简单，只需上传一个代码文件，通过网址访问，便可进行很多日常操作，极大地方便了使用者对网站和服务器的管理。正因如此，也有小部分人将代码修改后当作后门程序使用，以达到控制网站服务器的目的，**也可以将其称做为一种网页后门**

**最普通的一句话木马：**

<?php   @eval($_POST['shell']);?>

<?php system($_REQUEST['cmd']);>

![1647168572_622dcc3c8e5be2bdf77ed.png!small?1647168572799](https://image.3001.net/images/20220313/1647168572_622dcc3c8e5be2bdf77ed.png!small?1647168572799)

## 中国菜刀

中国菜刀（Chopper）是一款经典的网站管理工具，具有文件管理、数据库管理、虚拟终端等功能。

它的流量特征十分明显，现如今的安全设备基本上都可以识别到菜刀的流量。现在的菜刀基本都是在安全教学中使用。

github项目地址：[https://github.com/raddyfiy/caidao-official-version](https://github.com/raddyfiy/caidao-official-version)  

由于菜刀官方网站已关闭，现存的可能存在后门最好在虚拟机运行，上面项目已经进行了md5对比没有问题。

![1647168736_622dcce0ee65235dabe4e.png!small?1647168737325](https://image.3001.net/images/20220313/1647168736_622dcce0ee65235dabe4e.png!small?1647168737325)

### 菜刀webshell的静态特征

菜刀使用的webshell为一句话木马，特征十分明显

常见一句话(Eval)：

PHP, ASP, ASP.NET 的网站都可以：

> PHP:    <?php @eval($_POST['caidao']);?>
> 
> ASP:    <%eval request("caidao")%>
> 
> ASP.NET:    <%@ Page Language="Jscript"%><%eval(Request.Item["caidao"],"unsafe");%>

### 菜刀webshell的动态特征

请求包中：

ua头为百度爬虫

请求体中存在eavl，base64等特征字符

请求体中传递的payload为base64编码，并且存在固定的QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtpZihQSFBfVkVSU0lPTjwnNS4zLjAnKXtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO307ZWNobygiWEBZIik7J

请求体中执行结果响应为明文，格式为[X@Y    结果](mailto:%E5%B9%B6%E4%B8%94%E5%9C%A8X@Y./)   X@Y之中

![1647169656_622dd0781bd3f5e0ae199.png!small?1647169656466](https://image.3001.net/images/20220313/1647169656_622dd0781bd3f5e0ae199.png!small?1647169656466)

![1647169701_622dd0a59303415942bb8.png!small?1647169701877](https://image.3001.net/images/20220313/1647169701_622dd0a59303415942bb8.png!small?1647169701877)

## **蚁剑**

AntSword（蚁剑）是一个开放源代码，跨平台的网站管理工具，旨在满足渗透测试人员以及具有权限和/或授权的安全研究人员以及网站管理员的需求。

github项目地址： [https://github.com/AntSwordProject/antSword](https://github.com/AntSwordProject/antSword)  

![1647169735_622dd0c79624d24331faf.png!small?1647169735843](https://image.3001.net/images/20220313/1647169735_622dd0c79624d24331faf.png!small?1647169735843)

### 蚁剑webshell静态特征

[https://github.com/AntSwordProject/AwesomeScript](https://github.com/AntSwordProject/AwesomeScript)蚁剑官方为我们提供了制作好的后门，官方的脚本均做了不同程度“变异”，蚁剑的核心代码是由菜刀修改而来的，所有普通的一句话木马也可以使用。

Php中使用assert，eval执行, asp 使用eval ，在jsp使用的是Java类加载（ClassLoader）,同时会带有base64编码解码等字符特征

![1647170192_622dd290d6a8ca1ba57bf.png!small?1647170193460](https://image.3001.net/images/20220313/1647170192_622dd290d6a8ca1ba57bf.png!small?1647170193460)

### 蚁剑webshell动态特征

**默认编码连接时**

这里我们直接使用菜刀的一句话webshell

每个请求体都存在@ini_set(“display_errors”, “0”);@set_time_limit(0)开头。并且存在base64等字符

响应包的结果返回格式为  随机数 结果  随机数

![1647170363_622dd33b14182b1081659.png!small?1647170363388](https://image.3001.net/images/20220313/1647170363_622dd33b14182b1081659.png!small?1647170363388)

**使用base64编码器和解码器时**

![1647170543_622dd3efd9afd3e6d3ee7.png!small?1647170544145](https://image.3001.net/images/20220313/1647170543_622dd3efd9afd3e6d3ee7.png!small?1647170544145)

蚁剑会随机生成一个参数传入base64编码后的代码，密码参数的值是通过POST获取随机参数的值然后进行base64解码后使用eval执行

响应包的结果返回格式为  随机数 编码后的结果  随机数

![1647170560_622dd400c8203be11f45c.png!small?1647170561263](https://image.3001.net/images/20220313/1647170560_622dd400c8203be11f45c.png!small?1647170561263)

![1647170574_622dd40e76d5fd70dd9c2.png!small?1647170574792](https://image.3001.net/images/20220313/1647170574_622dd40e76d5fd70dd9c2.png!small?1647170574792)

## **冰蝎**

冰蝎是一款动态二进制加密网站管理客户端。

github地址：https://github.com/rebeyond/Behinder

![1647170705_622dd49185e0ab8d4cfd1.png!small?1647170705765](https://image.3001.net/images/20220313/1647170705_622dd49185e0ab8d4cfd1.png!small?1647170705765)

冰蝎文件夹中，server 文件中存放了各种类型的木马文件

![1647170725_622dd4a54fb0c5bfa44c6.png!small?1647170725592](https://image.3001.net/images/20220313/1647170725_622dd4a54fb0c5bfa44c6.png!small?1647170725592)

### 冰蝎webshell木马静态特征

这里主要分析3.0版本的

采用采用预共享密钥，密钥格式为md5(“admin”)[0:16], 所以在各种语言的webshell中都会存在16位数的连接密码，默认变量为k。

在PHP中会判断是否开启openssl采用不同的加密算法，在代码中同样会存在eval或assert等字符特征

![1647171068_622dd5fc62003abea147f.png!small?1647171068688](https://image.3001.net/images/20220313/1647171068_622dd5fc62003abea147f.png!small?1647171068688)

在aps中会在for循环进行一段异或处理

![1647170766_622dd4ce52c0785e2eaa2.png!small?1647170766623](https://image.3001.net/images/20220313/1647170766_622dd4ce52c0785e2eaa2.png!small?1647170766623)

在jsp中则利用java的反射，所以会存在ClassLoader，getClass().getClassLoader()等字符特征

![1647170932_622dd574b367b573c99bf.png!small?1647170933096](https://image.3001.net/images/20220313/1647170932_622dd574b367b573c99bf.png!small?1647170933096)

### 冰蝎2.0 webshell木马动态特征

在了解冰蝎3.0之前，先看看2.0是怎么交互等

2.0中采用协商密钥机制。第一阶段请求中返回包状态码为200，返回内容必定是16位的密钥

Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2![1647171493_622dd7a52508b5654fbf4.png!small?1647171493436](https://image.3001.net/images/20220313/1647171493_622dd7a52508b5654fbf4.png!small?1647171493436)

建立连接后 所有请求 Cookie的格式都为: Cookie: PHPSESSID=; path=/；

![1647171672_622dd858ad7a9cc4904db.png!small?1647171673147](https://image.3001.net/images/20220313/1647171672_622dd858ad7a9cc4904db.png!small?1647171673147)

### 冰蝎3.0 webshell木马动态特征

在3.0中改了，去除了动态密钥协商机制，采用预共享密钥，全程无明文交互，密钥格式为md5(“admin”)[0:16],但还是会存在一些特征

在使用命令执行功能时，请求包中content-length 为5740或5720（可能会根据Java版本而改变）

每一个请求头中存在Pragma: no-cache，Cache-Control: no-cache

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

![1647171814_622dd8e64e59b47c2e210.png!small?1647171814762](https://image.3001.net/images/20220313/1647171814_622dd8e64e59b47c2e210.png!small?1647171814762)

## **哥斯拉**

哥斯拉继菜刀、蚁剑、冰蝎之后具有更多优点的Webshell管理工具

[github地址：https://github.com/BeichenDream/Godzilla](https://github.com/BeichenDream/Godzilla)  

![1647171870_622dd91e7df2a0e35e913.png!small?1647171870876](https://image.3001.net/images/20220313/1647171870_622dd91e7df2a0e35e913.png!small?1647171870876)

哥斯拉的webshell需要动态生成，可以根据需求选择各种不同的加密方式

![1647171893_622dd935168bb389388b1.png!small?1647171893715](https://image.3001.net/images/20220313/1647171893_622dd935168bb389388b1.png!small?1647171893715)

### 哥斯拉webshell木马静态特征

选择默认脚本编码生成的情况下，jsp会出现xc,pass字符和Java反射（ClassLoader，getClass().getClassLoader()），base64加解码等特征

![1647171938_622dd962545b9fe2b3ffb.png!small?1647171938717](https://image.3001.net/images/20220313/1647171938_622dd962545b9fe2b3ffb.png!small?1647171938717)

php，asp则为普通的一句话木马

![1647171992_622dd9982fef522992b58.png!small?1647171992556](https://image.3001.net/images/20220313/1647171992_622dd9982fef522992b58.png!small?1647171992556)

### 哥斯拉webshell动态特征

所有请求中Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

所有响应中Cache-Control: no-store, no-cache, must-revalidate,

以上两个只能作为弱特征参考

同时在所有请求中Cookie中后面都存在；特征

![1647172209_622dda71557088a32cbf4.png!small?1647172209728](https://image.3001.net/images/20220313/1647172209_622dda71557088a32cbf4.png!small?1647172209728)