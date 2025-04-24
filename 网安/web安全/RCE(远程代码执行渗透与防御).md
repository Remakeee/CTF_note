远程代码执行：Remote Code Execute 
远程命令执行：Remote Command Execute

CVE-2021-3177 python RCE漏洞
CVE-2021-21972 VMWare RCE漏洞
CVE-2021-25646 Apache Druid RCE漏洞

CNVD-2020-46552 深信服EDR
CNVD-2021-30101 网康


**PHP RCE涉及函数**
命令commond注入
system()
exec("ls")/shell_exec()
pcntl_exec()
passthru()
popen()
proc_open()

**代码code注入**
eval()
assert()
preg_replace()
create_function()
call_user_func()/call_user_func_array()
usort()/uasort()

**Windows命令拼接符号**
&&——左边的命令执行成功，右边才执行
&——简单的拼接，左右有执行顺序，无条件
│——上一条命令的输入，作为下一条命令的输入
││——左边的命令执行失败，右边才执行



**Linux命令拼接符号**
;——没有任何逻辑关系的连接符
&&——左边的命令执行成功，右边才执行
│——上一条命令的输入，作为下一条命令的输入
││——左边的命令执行失败，右边才执行
&——任务后台执行




CTF练习[CTFHub](https://www.ctfhub.com/#/index)