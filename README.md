# 

## 前言

做APP体积瘦身 网页优化的时候，经常需要对图片压缩处理，以便帮助用户节省流量和提升网站加载速度。

图片压缩有很多方法，推荐使用[TinyPNG](https://tinypng.com/)。TinyPNG 是一个在线压缩工具，主要优点是在视觉上没有明显变化的情况下达到很高的压缩比。

TinyPNG官网: https://tinypng.com/

> TinyPNG支持一次最多上传20张图片，图片最大5M。

实际使用中往往有很多徐鹏需要压缩，仅仅一块网页上传图片压缩效率太低了，所以通过python脚本来批量压缩图片，将一个文件夹中的图片批量压缩，省时省力

## 使用方法

### 一.配置环境

**Python:** 安装 Python3 环境，(如果是Mac，则自带的有Python环境)。

**Tinify:** 导入Tinify

```
  pip3 install --upgrade tinify
```

### 二.申请 API key

到此处申请 API key: https://tinypng.com/developers

> 一个 key 每个月可以免费压缩500张图片，可以申请多个 key。

### 三.配置脚本并运行

下载完该脚本后，你需要简单编辑一下该脚本，将申请到到API key 填写进去。

```
tinify.key = "你申请到的API key"
```

之后你可以将该脚本放入到需要压缩的图片的文件夹下，然后在命令行(终端)中进入到该文件夹，执行如下命令即可:

```
python3 tinypng.py -d 文件夹
```

会递归查找图片文件夹并在当前目录下创建tiny文件夹，压缩图片会放置到tiny文件夹下

