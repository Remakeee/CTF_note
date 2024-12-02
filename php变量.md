---
tags:
  - PHP
title: php变量
---
# 特殊的变量[#](https://www.cnblogs.com/linfangnan/p/13521819.html#2892312890)

## 可变变量[#](https://www.cnblogs.com/linfangnan/p/13521819.html#1071586181)

一个可变变量 “$$” 获取了一个普通变量的值后，用这个值作为这个可变变量的变量名。一个美元符号表示提取变量中的值，而 2 个连续的美元符号表示用某个变量的内容作为变量名，再来访问该变量。例如以下代码：

Copy Highlighter-hljs

解释

`<?php $a = "b"; $b = "c"; $c = "a";  echo $a;      //输出 b echo $$a;      //输出 c echo $$$a;      //输出 a ?>`

## 超全局变量[#](https://www.cnblogs.com/linfangnan/p/13521819.html#4142454232)

PHP 的 **$ GLOBALS** 是一个超全局变量，它引用全局作用域中可用的全部变量。变量时一个包含了全部变量的全局组合数组，变量的名字就是数组的键。有时候当 flag 隐藏在某个变量中时，可以考虑从 GLOBALS 中得到。

# 变量覆盖[#](https://www.cnblogs.com/linfangnan/p/13521819.html#1020350144)

extract() 函数从数组中将变量导入到当前的符号表。使用数组键名作为变量名，使用数组键值作为变量值,针对数组中的每个元素将在当前符号表中创建对应的一个变量。extract() 函数也可以将 GET 传入的数据进行转换，例如：

Copy Highlighter-hljs

解释

`<?php $a = false; extract($_GET); if($flag) {       echo "flag{}" } ?>`

此时变量 a 已经被定义了，但是在 extract() 函数转换 GET 方法传入的数据时，传入的 a 在转换时就会把原来的变量覆盖掉。