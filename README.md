# 马原、毛概刷题工具
> 欢迎使用该题库进行二次开发！

本项目为马原、毛概的选择题刷题工具，题目大体按照章节顺序排布。如遇题目缺字、错字等问题，或者有功能上的建议，欢迎提`issue`反馈。

## 目录

```c++
.
├── archive
│   ├── flag //当前题目进度
│   ├── maogai.json //毛概题库
│   └── mayuan.json //马原题库
├── LICENSE //许可证
├── README.md //说明文档
└── test //主程序
```



## 功能

+ [x] 顺序刷题
+ [ ] 随机刷题
+ [ ] 考试模拟
+ [ ] 错题本

## 用法

Linux / Mac OS:

```bash
git clone git@github.com:jeasonlau/Question-test.git
cd ./Question-test
sudo chmod +x ./test
./test
```

Windows:

+ 拥有`python`环境：

  使用`git clone git@github.com:jeasonlau/Question-test.git`或点击`Download ZIP`下载该仓库，在仓库根目录下打开`cmd`/`powershell`，输入`python ./test`运行

+ 没有`python`环境：

  > 注:因本人没有Windows系统，打包可能不及时，版本会稍落后于`master`分支
  
  下载`release`中最新版本的`Source code`和`test.exe`，将`test.exe`放入`Source code`的根目录下，双击运行

