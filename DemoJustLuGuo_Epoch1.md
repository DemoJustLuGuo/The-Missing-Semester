# CFC Studio 共学 Epoch1 指引

---

# [DemoJustLuGuo]

## 笔记证明

### 01.06

#### 学习时长：50 分钟

跟着视频在进行基本命令行的学习 (使用 powershell)

在运行 ls -l 命令时 powershell 突然报错：

> Get-ChildItem: Missing an argument for parameter 'LiteralPath'. Specify a parameter of type 'System.String[]' and try again.

百度后发现错误是因为 Powershell 使用-LiteralPath，因为该选项与-l 匹配，但它需要一个参数。（这里应该是 windows 与 linux 命令使用的差异导致的）
查阅命令帮助后发现 powershell 可直接使用 ls 或 dir、gci 等命令列出文件目录

> 或者使用 ls -Path 'C:\Users\YourUsername\Documents'

在此之前使用查看环境变量 echo $PATH命令也遇到了同样的问题，不过在经过弹幕提醒后知道了windows的powershell使用的是$env:path 命令

总结：最近的时间比较紧，今天就先看到这里，使用 powershell 的原因是我忽视了 windows 与 linux 之间的区别，在学习之时被这些奇妙错误搞麻了，目前已老实安装 bash，等考试完后会补上接下来的课程的。
