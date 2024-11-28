下载arm架构java压缩包
![](图片/Pasted%20image%2020241001003308.png)

```python
open .bash_profile



# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/opt/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/opt/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# 复制如下内容，JAVA_HOME 替换为自己目录
export JAVA_17_HOME=/Users/boshanghanyancui/Applications/openjdk/jdk-17.0.2.jdk/Contents/Home/
export JAVA_8_HOME=/Users/boshanghanyancui/Applications/openjdk/jdk1.8.0_402.jdk/Contents/Home/
export JAVA_11_HOME=/Users/boshanghanyancui/Applications/openjdk/jdk-11.0.2.jdk/Contents/Home/
export JAVA_21_HOME=/Users/boshanghanyancui/Applications/openjdk/jdk-21.0.3.jdk/Contents/Home/
export PATH=$JAVA_HOME/bin:$PATH:.

alias jdk8='export JAVA_HOME=$JAVA_8_HOME'
alias jdk11='export JAVA_HOME=$JAVA_11_HOME'
alias jdk17='export JAVA_HOME=$JAVA_17_HOME'
alias jdk21='export JAVA_HOME=$JAVA_21_HOME'



source .bash_profile

```



``jdk8``
![](图片/Pasted%20image%2020241001003800.png)
``jdk11``
![](图片/Pasted%20image%2020241001003844.png)
``jdk17``
![](图片/Pasted%20image%2020241001003930.png)
``jdk21``
![](图片/Pasted%20image%2020241001004005.png)

