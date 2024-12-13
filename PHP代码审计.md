1. 全局代码审计
2. 敏感函数参数回溯
3. 定向功能分析
---
php运行模式
- CLI（命令行运行）
- PHP Build-in Webserver
- Apache  PHP-mod
- Swoole

----

php安全配置
- magic_quotes_gpc:5.3后废弃,5.4后废除
- regster_global:4.2后默认为false
- allow_url_include:默认false
- allow_url_fopen:默认false
- request_order:5.3后从GPC改为GP
- short_open_tag: 5.4后无论是否开启，<?=..?>总是可以被执行
- openbasedir:限制PHP可以访问那些目录
- disable_functions/disable_classes:限制PHP不能执行那些函数或者类
- enable_dll:是否允许加载PHP扩展

---
危险函数归纳

```php
include/require/include_once/require_once

eval/assert/preg_replace/create_function

system/passthru/exec/shell_exec

file_get_contents/fread/readfile/file/show_source

file_put_contents/fwrite/mkdir

unlink/rmdir

move_uploaded_file/copy/rename

extract/parse_str

simplexml_load_files/simplexal_load_string

unserialize

urldecode/base64_decode

```

代码执行函数
- eval 把字符串作为PHP代码执行，很多常见的webshell都是用eval来执行具体操作的

- assert 也是把字符串作为PHP代码执行

- preg_replace 是正则表达式函数


包含函数
- 文件包含函数主要作用为包含并运行指定文件

- include \$file,如果$file可控的情况下，我们就可以包含任意文件了，从而达到getshell的目的

- 包含函数也能够读取任意文件内容，这就需要用到支持的协议和封装协议和过滤器


文件操作函数
- copy：拷贝文件

- file_get_contents：将整个文件读入一个字符串

- file_put_contents：将一个字符串写入文件

- unlink：删除文件

- rmdir：删除目录


命令执行函数
- exec() 执行一个外部程序

- system() 执行外部程序，并且显示输出

- 只要命令就能执行的参数可控系统命令

----
SQL注入代码审计






