---
tags:
  - SQL
---
# 二次注入
二次注入是指已存储的数据库，文件的用户输入被读取后再次进入到SQL语句查询中导致的注入
二次注入的原理，在第一次进行数据库插入数据的时候，使用了 [[addslashes]] 、get_magic_quotes_gpc、mysql_escape_string、mysql_real_escape_string等函数对其中的特殊字符进行了转义