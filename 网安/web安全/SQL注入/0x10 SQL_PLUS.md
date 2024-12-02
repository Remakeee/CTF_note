---
tags:
  - SQL
  - CTF
  - web
title: SQL_PLUS
---



# 二次注入
二次注入是指已存储的数据库，文件的用户输入被读取后再次进入到SQL语句查询中导致的注入
二次注入的原理，在第一次进行数据库插入数据的时候，使用了 [[addslashes]] 、get_magic_quotes_gpc（[宽字节注入——魔术引号的绕过_魔术引号绕过-CSDN博客](https://blog.csdn.net/weixin_43264067/article/details/105945059)）、mysql_escape_string（[PHP: mysql_escape_string - Manual](https://www.php.net/manual/zh/function.mysql-escape-string.php)）、mysql_real_escape_string（[Sqli-labs Less-36 宽字节注入 绕过mysql_real_escape_string()函数转义 - zhengna - 博客园](https://www.cnblogs.com/zhengna/p/12661170.html)）等函数对其中的特殊字符进行了转义
例题：
[BUUCTF在线评测](https://buuoj.cn/challenges)——[[[CISCN2019 华北赛区 Day1 Web5]CyberPunk]]














# 无列名注入
在information_schema库杯过滤时，可以使用这种方法获得列名
[[SWPU2019]Web1 超详细教程-CSDN博客](https://blog.csdn.net/m0_74196038/article/details/142152701)



# 堆叠注入
没有过滤show，rename，alert时可以尝试使用堆叠注入