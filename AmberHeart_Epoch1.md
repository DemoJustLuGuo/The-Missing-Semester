# CFC Studio 共学 Epoch1 指引
---
# [AmberHeart]

## 笔记证明

### 01.11

#### 今日学习时间:40min
#### 学习内容小结:Windows和Linux的差异,很大


Let's study Shell!


先前有在Windows尝试用过PowerShell，大概是Shell的一种分支?


终端→显示Shell的窗口


拓展联想：cmd属于shell的一种吗?查找后：√


your platform plus like 'terminal' 发现已有打开后是类似powershell的界面?


该查找cmd,powerShell,terminal三者间的区别了


区别大概是：

①PowerShell以系统性管理任务进程为主,而Windows terminal则属于终端模拟器应用程序？

②PowerShell侧重于管理,Windows terminal则以开发,模拟环境为主？



test

①尝试使用echo输出带有空格的字符串

②尝试使用‘+’

③执行echo 283 + pro 输出如下

>283

>+

>pro

思考:echo的执行是将变量自前向后依次输出？

查找后发现用法近似感觉像是Python中的print,也可以执行程序


执行echo $path无输出

>查找后发现windows系统应执行echo $ENv:path

>输出成功


执行which echo报错

>which为linux命令

>查找后发现Windows类似命令Get-command

>输出成功


执行cd /home报错

>估计是绝对路径下linux与windows文件夹不同产生的差异问题,不打算进一步查询


执行cd -报错

>linux与windows的差异问题 老实用绝对路径回去了


执行ls -l报错

>老套的差异问题 查到-LiteralPath似乎有近似作用但是需要参数


执行ls 出现以下内容

>d-----      ...

>d-----      ...

>d-r---      ...

>dar---      ...

>d-r---      ...

>dar--l      ...

不同于linux的前缀 查找后发现下列关系

d 目录

r 可读

w 可写

a 全体用户

吧大概

l什么意思没查到就是了


总结:大部分时间和精力花在了解决Linux与Windows的系统差异上,等安装wsl整好bash后提速应该就会很快了,总之摸鱼摸爽了

总结:摸了