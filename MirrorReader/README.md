# MirrorReader

[English version](../docs/en/mirrorreader.md)

MirrorReader 是 MirrorMind 的一个最小阅读原型。它先解决一个具体问题：阅读被中断后，如何更容易继续，而不是一开始就做复杂的 AI 阅读软件。

## 当前阶段：阶段 1

目前只实现最基础的连续翻页：

- 读取 UTF-8 编码的 TXT 文件；
- 按空行切分段落；
- 显示当前段落和总段落数；
- 使用命令查看上一段或下一段；
- 在第一段和最后一段进行边界保护；
- 输入命令退出程序。

当前阶段暂不保存阅读进度，也不记录笔记和认知快照。这些属于后续阶段。

## 运行方法

需要 Python 3.10 或更高版本。进入本目录后运行：

```powershell
python main.py
```

默认读取 `sample_data/sample_article.txt`。也可以传入自己的 UTF-8 TXT 文件：

```powershell
python main.py "D:\路径\文章.txt"
```

## 阅读命令

```text
n       下一段
p       上一段
s       查看当前进度
help    查看帮助
exit    退出程序
```

## 项目边界

V0 不做登录、云同步、网页抓取、OCR、图形界面、自动状态识别或自主 Agent。完整设计与后续路线见 `MirrorReader开发指引.md`。

