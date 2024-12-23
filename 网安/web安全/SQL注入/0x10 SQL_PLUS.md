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













[[强网杯 2019]随便注 - chalan630 - 博客园](https://www.cnblogs.com/chalan630/p/12583667.html)


## 绕过select
如果无法使用select，还是获得不了flag，可以通过预编译的方式绕过对select的限制。
> SQL 语句的执行处理  
> 1、即时 SQL  
> 　　一条 SQL 在 DB 接收到最终执行完毕返回，大致的过程如下：
> 
> 　　1. 词法和语义解析；  
> 　　2. 优化 SQL 语句，制定执行计划；  
> 　　3. 执行并返回结果；  
> 如上，一条 SQL 直接是走流程处理，一次编译，单次运行，此类普通语句被称作 Immediate Statements （即时 SQL）。
> 
> 2、预处理 SQL  
> 　　但是，绝大多数情况下，某需求某一条 SQL 语句可能会被反复调用执行，或者每次执行的时候只有个别的值不同（比如 select 的 where 子句值不同，update 的 set 子句值不同，insert 的 values 值不同）。如果每次都需要经过上面的词法语义解析、语句优化、制定执行计划等，则效率就明显不行了。  
> 　　所谓预编译语句就是将此类 SQL 语句中的值用占位符替代，可以视为将 SQL 语句模板化或者说参数化，一般称这类语句叫Prepared Statements。  
> 　　预编译语句的优势在于归纳为：一次编译、多次运行，省去了解析优化等过程；此外预编译语句能防止 SQL 注入。

预处理流程
```sql
SET;									# 用于设置变量名和值
PREPARE stmt_name FROM preparable_stmt;	# 用于预备一个语句，并赋予名称，以后可以引用该语句
EXECUTE stmt_name;			 			# 执行语句
{DEALLOCATE | DROP} PREPARE stmt_name;	# 用来释放掉预处理的语句
```













