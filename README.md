<h1 align="center">- 马原毛概刷题工具 -</h1>
![screenshot](./picture/screenshot.svg)
<p align="center">
<img src="https://img.shields.io/badge/language-python-blue.svg?longCache=true&style=for-the-badge">
<img src="https://img.shields.io/badge/license-MIT-orange.svg?longCache=true&style=for-the-badge">
<img src="https://img.shields.io/badge/version-v0.0.3-red.svg?longCache=true&style=for-the-badge">
</p>

## 介绍
> 该项目题库使用`json`格式存储，欢迎使用该题库进行二次开发！

本项目为马原、毛概的选择题刷题工具，题目大体按照章节顺序排布。如遇题目缺字、错字等问题，或者有功能上的建议，欢迎提`issue`反馈。

## 目录

```c++
.
├── archive
│   ├── *.error //错题本
│   ├── *.flag //刷题进度
│   └── *.json //题库
├── func
│   ├── __init__.py //package标识
│   ├── file.py //文件存取
│   ├── question.py //题目输出
│   ├── order.py //顺序刷题
│   ├── random.py //随机刷题
│   ├── exam.py //考试模拟
│   └── error.py //错题存取
├── LICENSE //许可证
├── README.md //说明文档
└── test //主程序

```



## 功能

+ [x] 顺序刷题
+ [x] 随机刷题
+ [x] 考试模拟
+ [x] 错题本

## 用法

Linux / Mac OS:

```bash
git clone https://github.com/jeasonlau/Question-test
cd ./Question-test
sudo chmod +x ./test
./test
```

Windows:

+ 拥有`python`环境：

  使用`git clone https://github.com/jeasonlau/Question-test`或点击`Download ZIP`下载该仓库，在仓库根目录下打开`cmd`/`powershell`，输入`python ./test`运行

+ 没有`python`环境：

  > 注:因本人没有Windows系统，打包可能不及时，版本会稍落后于`master`分支
  
  下载`release`中最新版本的`Source code`和`test.exe`，将`test.exe`放入`Source code`的根目录下，双击运行

