题目可能有些问题 不确定
整体就是sqlmap盲注就行
可能会尝试burpsuite手工注入
找到了flag 但是提交是错误
2024.12.23 目前没看到正解



![](图片/Pasted%20image%2020241223143553.png)
使用admin&admin尝试发现网页没有回显
所以使用BP抓包，在账号处使用sql注入，比较回显
![](图片/Pasted%20image%2020241223152420.png)
![](图片/Pasted%20image%2020241223152440.png)
![](图片/Pasted%20image%2020241223153250.png)
有报错可知有注入点
尝试用sql注入过滤字典进行攻击，查看被过滤字符
![](图片/Pasted%20image%2020241223153116.png)
发现information和column被过滤，怀疑information_schema被过滤，需要找绕过方法















