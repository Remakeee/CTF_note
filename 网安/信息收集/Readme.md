---
profileName: Remakeee
postId: "101"
categories:
  - 12
tags:
  - CTF
---
# 域名相关信息
1. whois cnnic
2. kali 自带whois
3. ICP备案
4. 获得 邮箱（可以钓鱼） 手机号 姓名 反查更多的域名
5. 企业查 天眼查
6. 子域名
    1. oneforall（kali）
    2. layer（windows）
    3. [web查子域名](http://phpinfo.me/domain)这个网站好像没了
        1. https://site.ip138.com
    4. [证书查](https://crt.sh/)
    3. subdomainsburte （在桌面）
        1. `python subDomainsBrute.py xxx.com`
    4. 微步
7. DNS信息
    1. ([Subdomain - RapidDNS Rapid DNS Information Collection](https://rapiddns.io/subdomain))
    2. ![](图片/Pasted%20image%2020240815163617.png)
    3. [dbcha.com](https://dbcha.com)
    4. [What's that site running? | Netcraft](https://sitereport.netcraft.com/)

---

# ip相关信息
1. ping / nslookup
2. ip归属信息
    1. http://ipwhois.cnnic.net.cn
3. CDN(内容分发)
    1. 实现流程(以阿里云为例)1. https://www.zhihu.com/question/36514327/answer/1604554133
        1. 当终端用户(北京)向www.a.com下的指定资源发起请求时，首先向LDNS(本地DNS)发起域名解析请求。
        2. LDNS检查缓存中是否有www.a.com的IP地址记录。如果有，则直接返回给终端用户;如果没有，则向授权DNS查询。
        3. 当授权DNS解析www.a.com时，返回域名CNAMEwww.a.tbcdn.com对应IP地址。
        4. 域名解析请求发送至阿里云DNS调度系统，并为请求分配最佳节点IP地址。
        5. LDNS获取DNS返回的解析IP地址。
        6. 用户获取解析IP地址。
        7. 用户向获取的IP地址发起对该资源的访问请求。
    2. 找到真实ip
        1. 超级ping     [多个地点Ping服务器,网站测速 - 站长工具 (chinaz.com)](https://ping.chinaz.com/)
        2. 历史DNS [DNS History](https://dnshistory.org/)
        3. 通过子域名查询ip 
            1. 子域名和主域名放在同一服务器，没有使用CDN解析
        4. 国外主机解析
            1. https://www.webpagetest.org/
        5. 其他，比如邮件、ssl证书、手机app抓包、网络空间搜索引擎等等

---

# 端口服务相关信息
1. 端口扫描思路和代码实现
    1. telent
    2. wget
    3. nc -vz
    4. 代码
```python
import socket, threading

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''

def scan_ports(host_ip, delay):

    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing purposes

    # Spawning threads to scan ports
    # 先扫10000个端口
    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(10000):
        threads[i].start()

    # Locking the script until all threads complete
    for i in range(10000):
        threads[i].join()

    # Printing listening ports from small to large
    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])

def main():
    host_ip = input("Please enter host IP: ")
    # 超时抛出异常
    delay = int(input("How many seconds the socket is going to wait until timeout: "))   
    scan_ports(host_ip, delay)
    input("Press Any Key to Exit")

if __name__ == "__main__":
    main()
```
## 常见端口及漏洞
### 文件共享服务端口
|          |                           |                       |
| -------- | ------------------------- | --------------------- |
| 端口号      | 端口说明                      | 攻击方向                  |
| 21/22/69 | FTP/SFTP文件传输协议            | 允许匿名上传、下载、爆破<br>和嗅探操作 |
| 2049     | NFS服务(Network File System | 配置不当                  |
| 139      | Samba服务                   | 爆破、未授权访问、远程代<br>码和执行  |
| 389      | LDAP目录访问协议                | 注入、允许匿名访问、弱口<br>令     |
### 远程连接服务端口
| 端口号  | 端口说明             | 攻击方向                                |
| ---- | ---------------- | ----------------------------------- |
| 22   | SSH远程连接          | 爆破、SSH隧道及内网代理转发、 文件传输               |
| 23   | Telnet远程连接       | 爆破、嗅探、弱口令                           |
| 3389 | RDP远程桌面连接        | Shift后门(Windows Server2003以下的系统)、爆破 |
| 5900 | VNC              | 弱口令爆破                               |
| 5632 | PcAnywhere远程控制服务 | 抓密码、代码执行                            |
### web应用服务端
| 端口号         | 端口说明                      | 攻击方向                |
| ----------- | ------------------------- | ------------------- |
| 80/443/8080 | 常见的web服务端口                | Web攻击、爆破、对应服务 器版本漏洞 |
| 7001/7002   | Weblogic控制台               | Java反序列化、弱口令        |
| 8080/8089   | Jboss/resin/jetty/Jenkins | 反序列化、控制台弱口令         |
| 9090        | Websphere控制台              | Java反序列化、弱口令        |
| 4848        | Glassfish控制台              | 弱口令                 |
| 1352        | Lotus domino邮件服务          | 弱口令、信息泄露、爆破         |
| 10000       | Webmin-web控制面板            | 弱口令                 |
### 数据库服务端口
| 端口号         | 端口说明           | 攻击方向             |
| ----------- | -------------- | ---------------- |
| 3306        | MySQL          | 注入、提权、爆破         |
| 1433        | MSSQL数据库       | 注入、提权、SA弱口令      |
| 1521        | Oracle数据库      | TNS爆破、注入、反弹shell |
| 5432        | PostgreSQL数据库  | 爆破、注入、弱口令        |
| 27017/27018 | MongoDB        | 爆破、未授权访问         |
| 6379        | Redis数据库       | 可尝试未授权访问、弱口令爆破   |
| 5000        | Sysbase/DB2数据库 | 爆破、注入            |
### 邮件服务端口
| 端口号 | 端口说明     | 攻击方向  |
| --- | -------- | ----- |
| 25  | SMTP邮件服务 | 邮件伪造  |
| 110 | POP3协议   | 爆破、嗅探 |
| 143 | IMAP协议   | 爆破    |
### 网络常见协议端口
| 端口号   | 端口说明    | 攻击方向                  |
| ----- | ------- | --------------------- |
| 53    | DNS域名系统 | 允许区域传送、DNS劫持、 缓存投毒、欺骗 |
| 67/68 | DHCP服务  | 劫持、欺骗                 |
| 161   | SNMP协议  | 爆破、搜集目标内网信息           |
### 特殊服务端口
| 端口号         | 端口说明                   | 攻击方向        |
| ----------- | ---------------------- | ----------- |
| 2181        | Zookeeper服务            | 未授权访问       |
| 8069        | Zabbix服务               | 远程执行、SQL注入  |
| 9200/9300   | ElasticSearch服务        | 远程执行        |
| 11211       | Memcached服务            | 未授权访问       |
| 512/513/514 | Linux Rexec服务          | 爆破、rlogin登录 |
| 873         | Rsync服务                | 匿名访问、文件上传   |
| 3690        | SVN服务                  | SVN泄露、未授权访问 |
| 50000       | SAP Management Console | 远程执行        |

## 端口扫描工具
### nmap
- nmap.org/man/zh/man-output.html
- 扫描主机
- 扫描端口
- 探测操作系统、软件版本

---

# 指纹信息
- 通过关键特征，识别出目标的CMS系统、服务器、开发语言、操作系统、CDN、WAF的类别版本等
1. **CMS信息**:比如Discuz、织梦、帝国CMS、PHPCMS、ECshop等; 
2. 前端技术:比如HTML5、jquery、bootstrap、Vue、ace等; 
3. 开发语言:比如PHP、Java、Ruby、Python、C#等; 
4. Web服务器:比如Apache、 Nginx、IIS、lighttpd等; 
5. 应用服务器:比如Tomcat、Jboss、Weblogic、Websphere等; 
6. 操作系统信息:比如Linux、win2k8、win7、Kali、Centos等; 
7. **CDN信息**:是否使用CDN，如cloudflare、帝联、蓝讯、网宿、七 牛云、阿里云等; 
8. **WAF信息**:是否使用WAF，如D盾、云锁、宝塔、安全狗、360等
## CMS
- 内容管理系统
### 各类网站开源CMS
- 企业建站系统:MetInfo(米拓)、蝉知、SiteServer CMS等;  
- B2C商城系统:商派Shopex、ECshop、HiShop、XpShop等;  
- 门户建站系统:DedeCMS(织梦)、帝国CMS、PHPCMS、动易、CmsTop等;  
- 博客系统:WordPress、Z-Blog等;  
- 论坛社区:Discuz、PHPwind、WeCenter等;  
- 问答系统:Tipask、whatsns等;  
- 知识百科系统:HDwiki;  
- B2B门户系统:Destoon、B2Bbuilder、友邻B2B等; l 人才招聘网站系统:骑士CMS、PHP云人才管理系统; l 房产网站系统:FangCms等;  
- 在线教育建站系统:Kesion、EduSoho;  
- 电影网站系统:苹果CMS、ctcms、movcms等;  
- 小说文学建站系统:杰奇CMS;
### CMS识别思路
- 版本信息
- 特定文件MD5值
    - [Lucifer1993/cmsprint: CMS和中间件指纹库 (github.com)](https://github.com/Lucifer1993/cmsprint)
- 查看网页源代码
    - url/robots.txt
    - https://developers.google.cn/search/docs/crawling-indexing/robots/robots_txt?hl=zh-cn
- 通过特定文件分析
### CMS识别工具
- kali——whatweb
- 插件——Wappalyzer:https://www.wappalyzer.com
- 插件——whatruns :https://www.whatruns.com/
- 在线网站—— http://whatweb.bugscaner.com
- 在线网站—— http://finger.tidesec.com/
- https://github.com/Tuhinshubhra/CMSeeK 可以kali

---

# WAF识别
- web应用防火墙
- 过滤HTTP/HTTPS的请求
## 作用
- SQL Injection (SQLi)：阻止SQL注入
- Cross Site Scripting (XSS)：阻止跨站脚本攻击
- Local File Inclusion (LFI)：阻止利用本地文件包含漏洞进行攻击
- Remote File Inclusione(RFI)：阻止利用远程文件包含漏洞进行攻击
- Remote Code Execution (RCE)：阻止利用远程命令执行漏洞进行攻击
- PHP Code Injectiod：阻止PHP代码注入
- HTTP Protocol Violations：阻止违反HTTP协议的恶意访问
- HTTPoxy：阻止利用远程代理感染漏洞进行攻击
- Sshllshock：阻止利用Shellshock漏洞进行攻击
- Session Fixation：阻止利用Session会话ID不变的漏洞进行攻击
- Scanner Detection：阻止黑客扫描网站
- Metadata/Error Leakages：阻止源代码/错误信息泄露
- Project Honey Pot Blacklist：蜜罐项目黑名单
- GeoIP Country Blocking：根据判断IP地址归属地来进行IP阻断
## 识别思路
- github：Awesome-WAF https://github.com/0xInfection/Awesome-WAF
- 额外的cookie；
- 任何响应或请求的附加标头；
- 响应内容（如果被阻止请求）；
- 响应代码（如果被阻止请求）；
- IP地址（云WAF）；
- JS客户端模块（客户端WAF）
- xsstring = '<script>alert("XSS");</script>' 
- sqlistring = "UNION SELECT ALL FROM information_schema AND ' or SLEEP(5) or '"
- lfistring = '../../../../etc/passwd' rcestring = '/bin/cat /etc/passwd; ping 127.0.0.1; curl google.com' 
- xxestring = '<!ENTITY xxe SYSTEM "file:///etc/shadow">]><pwn>&hack;</pwn>'
- wafw00f---kali
- ![](图片/Pasted%20image%2020240912142906.png)

---

# Google Hacking（搜索引擎）
1. site：找到与指定网站有联系的URL
2. intitle：返回所有网页标题中包含关键词的网站 （admin之类的）
3. inurl：只搜索网页链接含有关键词的页面
4. intext：只搜索网页正文部分含有关键词的页面
5. https://www.google.com/advanced_search
## 语法数据库
- https://www.exploit-db.com/google-hacking-database
- https://github.com/BullsEye0/google_dork_list

---

# 网络空间搜索引擎
物联网？
osint 开源网络情报
https://osintframework.com/
- 实时威胁地图
    - https://cybermap.kaspersky.com/
- 引擎
    - shodan
        - https://www.shodan.io/
        - ![](图片/Pasted%20image%2020240912202231.png)
        - ![](图片/Pasted%20image%2020240912202359.png)
        - ![](图片/Pasted%20image%2020240912202451.png)
        - ![](图片/Pasted%20image%2020240912202927.png)
        - https://github.com/random-robbie/My-Shodan-Scripts?tab=readme-ov-file
        - https://github.com/jakejarvis/awesome-shodan-queries
    - censys
        - https://search.censys.io/
    - zoomeye
        - https://www.zoomeye.hk/
    - 集成工具
        - https://github.com/knownsec/Kunyu
            - https://github.com/knownsec/Kunyu/blob/main/doc/README_CN.md 下载文档
        - https://github.com/coco413/DiscoverTarget
        - https://github.com/saucer-man/saucerframe

---

# 目录扫描
## 常见的敏感目录和文件
- robots.txt
- sitemap.txt
- 网站的备份文件/数据
    - 在线压缩
        - 路径
        - 文件名
        - wwwroot---20240914.zip
    - 帝国备份王
        - 1.sql---1.zip
- 后台登陆的目录
    - /admin
    - /mangage
- 安装包（源码）
    - 非开源，商用
    - 1.zip
- 上传的目录
    - 文件上传漏洞---webshell
    - /upload
    - /upload.php
- mysql的管理页面
    - web页面管理---phpadnin
- 程序的安装路径
    - /insatll
- php的探针
    - phpinfo
    - 雅黑探针
- 文本编辑器
    - Ueditor
    - kindeditor
    - CKeditor
    - 文件上传漏洞，命令注入
- Linux
    - /etc/passwd
    - /etc/shadow---SHA512
    - /etc/sudoers---sudo
- Macos
    - .DS_Store
- 编辑器的临时文件.swp
- 目录穿越
    - Windows IIS
    - apache
    - pikachu靶场
        - http://localhost/pikachu/vul/dir/dir_list.php?title=jarheads.php
        - http://localhost/pikachu/vul/dir/dir_list.php?title=../../../../Windows/win.ini
- tomcat WEB-INF
    - WEB-INF/web.xml : Web应用程序配置文件, 描述了servlet和其他的应用组件配置及命名规则.
    - WEB-INF/database.properties : 数据库配置文件
    - WEB-INF/classes/ : 一般用来存放Java类文件(.class)
    - WEB-INF/lib/ : 用来存放打包好的库(.jar)
    - WEB-INF/src/ : 用来放源代码(.asp和.php等)
- 其他非常规文件
    - secret.txt
    - password.txt
    - ...
## 扫描思路
- 直接加文件名
![](图片/Pasted%20image%2020240913154626.png)
- 扫描方法
    - 递归
        - dir xxx
    - 字典
    - 爆破
        - 1位
            - a-z
            - 0-9
        - 2位
            - aa
            - 00
            - a0
            - 9z
    - 爬虫
        - robots.txt
        - sitemap.xlml
        - 网页中的其他链接
    - fuzz（模糊测试）
        - 字典
            - /word 
            - /index.php?word=
- 文件扫描的字典
    - kali 
        - wordlists
    - **dirb**
        - /usr/share/wordlists/dirb/common.txt
- owasp

---

# Git hack
## git文件结构
## github搜索技巧
- kali in:file 搜索文件中包含kali的代码
- kali in:path 搜索路径中包含kali的代码
- kali in:path,file 搜索路径、文件中包含kali的代码
- shodan language:python 搜索关键字shodan，语言为python的代码
- filename:config.php language:php 搜索文件名为config.php，且语言为php
- kali topics:>=5 标签数量大于等于5的
- kali size:<1000 文件小于1KB的
- kali stars:10..50 star大于10小于50的
- kali pushed:>2021-08-15 搜索在2021年8月15日之后提交的
- kali pushed:2021-07-01..2021-08-01 搜索在此区间
- kali created:>=2021-06-01 创建时间
- kali pushed:<2021-08-01 -language:java 搜索在2020年8月1日前push代码且排除java语言
## git泄露利用方式
- 找到.git
    - 目录扫描
    - robots.txt
    - 搜索引擎搜索 intitle:"Index of /.git"
- 把.git下载到本地
    - https://github.com/BugScanTeam/GitHack --- python GitHack.py xxx.com/.git/
    - https://github.com/lijiejie/GitHack
    - https://github.com/wangyihang/githacker
    - https://github.com/WangWen-Albert/JGitHack
- 用git的命令获取内容
    - git log
    - git reset --hard [log hash]
    - git diff
- 工具 https://github.com/gakki429/Git_Extract
# kali工具
- 软件清单 https://tools.kali.org/tools-listing
- 中文翻译 https://github.com/Jack-Liang/kalitools
## 存活主机识别
- arping 
    - 将ARP和/或ICMP请求发送到指定的主机
    - [arping命令详解 - 五月的麦田 - 博客园 (cnblogs.com)](https://www.cnblogs.com/xzongblogs/p/14391379.html)
    - ![](图片/Pasted%20image%2020240915233433.png)
- fping
    - fping可以在命令行中指定要ping的主机数量范围
    - [fping的使用简介 - paul_hch - 博客园 (cnblogs.com)](https://www.cnblogs.com/paul8339/p/15175976.html)
    - [fping](fping.md)
- hping3
    - TCP/IP数据包组装/分析工具
    - 可以发起flood攻击
    - [hping3 使用详解 - liuxinyu123 - 博客园 (cnblogs.com)](https://www.cnblogs.com/liuxinyustu/articles/12808972.html)
- masscan 
    - 最快的互联网端口扫描器
    - ![](图片/Pasted%20image%2020240916105547.png)
- thcping6
    - atk6-thcping6
    - 可以攻击IPV6和ICMP6固有的协议弱点
## 路由分析
- netdiscover
    - 基于ARP的网络扫描工具
    - 地址解析协议，即ARP（Address ResolutionProtocol），是根据IP地址获取物理地址的一个TCP/IP协议
- netmask 
    - netmask可以在 IP范围、子网掩码、cidr、cisco等格式中互相转换
## 情报分析
- maltego 信息收集和网络侦查工具
- spiderfoot 收集信息和探测资源
- theharvester
    - 从公开来源收集电子邮件帐户和子域名的工具 OSINT
    - theHarvester -d microsoft.com -l 500 -b baidu
## 网络扫描
- masscan
- nmap
    - 主机发现
    - 端口扫描
    - 服务和版本探测
    - 操作系统探测
    - 防火墙/IDS躲避和哄骗
## DNS分析
- dnsenum 多线程perl脚本枚举域的DNS信息并发现非连续的IP段工具
- dnsrecon
    - DNS枚举和扫描
    - dnsrecon -d www.coolshell.cn
- fierce
    - DNS扫描程序
    - fierce --domain www.coolshell.cn
## IDS/IPS识别
- IDS （入侵检测系统） Intrusion Detection Systems
- IPS （入侵防御系统） Intrusion Prevention System
- lbd
    - load balance detector
    - CDN、负载均衡识别
    - lbd www.coolshell.cn
- wafw00f
    - WAF识别
    - wafw00f www.coolshell.cn
## SMB分析
- SMB：Server Message Block 网络文件系统协议
- enum4linux
    - 可以收集Windows系统的大量信息，如用户名列表、主机列表、共享列表、密码策略信息、工作组和成员信息、主机信息、打印机信息等等
    - enum4linux 192.168.142.1
- nbtscan
    - 扫描开放的NETBIOS名称服务器
    - nbtscan -r 192.168.142.0/24
- smbmap
    - SMBMap允许用户枚举整个域中的samba共享驱动器。 列出共享驱动器，驱动器权限，共享内容，上载/下载功能，文件名自动下载模式匹配，甚至执行远程命令
    - smbmap -u wuya -p 1234 -H 192.168.142.1
## SNMP分析
- 简单网络管理协议 大部分的设备都支持SNMP协议
- onesixtyone
    - 通过SNMP服务，渗透测试人员可以获取大量的设备和系统信息
    - onesixtyone 192.168.142.1
- snmp-check snmp-check 192.168.142.1 -p 161
## SSL分析
- ssldump SSL/TLS 网络协议分析工具
- sslh
    - 一款采用 C 语言编写的开源端口复用软件
    - SSLH 允许我们在 Linux 系统上的同一端口上运行多个程序/服务
- sslscan
    - 评估远程 Web 服务的 SSL/TLS 的安全性
    - sslscan www.coolshell.cn
- sslyze
    - 可以扫描出SSL中一些经典的配置错误
    - sslyze www.coolshell.cn
## 其他一些工具
dmitry --- 信息收集工具 子域，电子邮件地址，正常运行时间信息，tcp端口扫描，whois
ike-scan --- VPN服务嗅探工具
legion --- 使用NMAP，whataweb，nikto，Vulners，Hydra，SMBenum，dirbuster，sslyzer，webslayer等进行自动侦查和扫描