# GitHub 初学者路线指南

> 适用对象：刚开始学习编程，希望通过真实项目进入开发环境与开源社区的初学者。

## 1. 先区分 Git 和 GitHub

- **Git**：安装在电脑上的版本管理工具，用来记录代码如何变化。
- **GitHub**：托管 Git 仓库、展示项目、交流和协作的网站。

即使没有 GitHub，也可以在本地使用 Git；把本地仓库推送到 GitHub 后，才能获得远程备份、项目展示和社区协作能力。

## 2. 十个基础概念

| 概念 | 含义 |
|---|---|
| Repository | 一个项目仓库 |
| Commit | 一次带说明的版本快照 |
| Branch | 一条独立修改路线 |
| Remote | GitHub 上的远程仓库 |
| Clone | 把远程仓库下载到电脑 |
| Push | 把本地提交上传到 GitHub |
| Pull | 获取远程仓库的新提交 |
| Fork | 在自己账号下复制别人的仓库 |
| Issue | 报告问题、讨论需求 |
| Pull Request | 请求维护者合并你的修改 |

`Star` 只是收藏，不代表已经下载、学习或掌握该项目。

## 3. 最重要的安全规则

### 3.1 绝对不要上传密钥

不要提交：

- API Key、Token；
- 账号和密码；
- `.env` 文件；
- 数据库连接密码；
- 中转站密钥；
- 私人聊天记录和身份信息。

即使后来从仓库中删除，密钥也可能继续存在于 Git 历史里。密钥一旦误传，应立即去对应平台撤销，并生成新密钥。

### 3.2 不要上传无关文件

Python 项目常见 `.gitignore`：

```gitignore
__pycache__/
.venv/
.env
private_data/
*.log
```

不要公开上传受版权保护的完整文章、书籍或课程材料。仓库中只放自己编写或明确允许公开的示例文件。

### 3.3 提交前先检查

每次提交前运行：

```bash
git status
git diff
```

确认将要提交的文件中没有密钥、私人内容和无关的大文件。

初期尽量明确添加文件：

```bash
git add README.md
git add main.py
```

不要习惯性使用 `git add .`，以免误传所有文件。

## 4. 提交应该小而清晰

一次 Commit 尽量只完成一件事。

较好的提交说明：

```text
feat: add article paragraph splitting
feat: save reading position
fix: prevent position overflow
docs: explain how to run the project
```

不建议：

```text
改了一些东西
最终版
111
```

常见前缀：

- `feat`：增加功能；
- `fix`：修复问题；
- `docs`：修改文档；
- `test`：增加或修改测试；
- `refactor`：整理代码但不改变功能。

## 5. 初学阶段谨慎使用的命令

没有理解含义前，不要随便运行：

```text
git reset --hard
git push --force
git clean
git rebase
```

这些命令可能丢失本地修改或覆盖远程历史。遇到 Git 问题时，先运行：

```bash
git status
```

保留完整输出，再分析下一步，不要连续尝试网上找到的“万能修复命令”。

## 6. 推荐学习路线

### 第一阶段：管理自己的项目

先掌握：

```bash
git status
git diff
git add 文件名
git commit -m "提交说明"
git log --oneline
```

目标：能用 Git 保存自己项目的每个小进展。

### 第二阶段：连接 GitHub

再学习：

```bash
git remote
git push
git pull
git clone
```

目标：换电脑后仍能从 GitHub 获取项目，并理解本地仓库和远程仓库的关系。

### 第三阶段：阅读开源项目

不要一开始试图看懂全部代码。按照以下顺序：

1. 阅读项目简介；
2. 查看 README；
3. 找到安装和运行说明；
4. 成功运行项目；
5. 找到程序入口；
6. 修改一个很小的地方；
7. 查看修改前后的差异。

能够成功运行并找到入口，已经是有效进步。

### 第四阶段：参与社区

从低风险贡献开始：

- 修正文档错误；
- 补充使用说明或中文说明；
- 复现并报告问题；
- 改进示例代码；
- 修复一个范围明确的小问题。

之后再系统学习：

- 创建功能分支；
- Fork 项目；
- 提交 Pull Request；
- 根据维护者意见修改代码。

## 7. 日常最小工作流

开始开发前：

```bash
git status
git pull
```

完成一个小功能后：

```bash
git status
git diff
git add README.md
git add main.py
git commit -m "feat: add paragraph navigation"
git push
```

每次 Commit 前确认：

1. 程序能够运行；
2. 自己知道这次修改了什么；
3. 没有提交密钥和私人文件；
4. 提交说明能够让未来的自己看懂。

## 8. Star、Clone 和 Fork 怎么选

- 只是以后想看：使用 **Star**；
- 想在本地运行和学习：使用 **Clone**；
- 想修改并向原项目贡献：通常先 **Fork**，再 Clone 自己的 Fork；
- 只是下载一次代码：可以下载 ZIP，但无法方便地跟踪后续更新。

不要把所有 Star 的仓库都 Clone 到电脑。只下载当前真正学习的项目，并优先放在空间更充足的 D 盘。

## 9. 如何判断一个开源项目是否适合学习

优先选择：

- README 清晰；
- 有明确安装步骤；
- 最近仍有维护；
- 有示例和测试；
- 使用了你正在学习的语言；
- 项目规模没有大到完全无法定位入口；
- License 明确。

查看别人的代码不代表可以随意复制或商用。使用前应阅读项目的 License；如果不知道某个许可证允许什么，不要自行猜测。

## 10. 初学者常见误区

### 收藏等于学习

Star 只是资料管理。真正学习至少包括：运行、修改、解释和应用。

### 必须学完整个 Git 才能开始

没有必要。先掌握 `status → diff → add → commit → push`，其余能力按实际需要学习。

### 提交越大越专业

相反，小而清楚的提交更容易检查、理解和撤销。

### GitHub 只是放代码的网盘

GitHub 还记录项目演化、问题讨论、协作过程和开发者的工作方式。

### 一开始就追求很多贡献

先建立稳定完成个人项目的能力。高质量的小项目比大量浅层仓库更有价值。

## 11. 现在的具体起点：MirrorReader

可以把 MirrorReader 作为第一个长期使用 GitHub 的项目：

1. 创建仓库，初期可以设为 Private；
2. 编写 README，说明它解决什么问题；
3. 创建 Python `.gitignore`；
4. 编写最小程序：读取 TXT 并统计段落；
5. 完成第一次 Commit；
6. 推送到 GitHub；
7. 每完成一个小功能提交一次。

建议提交顺序：

```text
docs: describe MirrorReader v0
feat: load text article
feat: split article into paragraphs
feat: navigate between paragraphs
feat: save reading position
feat: restore previous session
```

第一阶段不以获得 Star 为目标，而是让仓库清楚展示：

```text
项目为什么存在
→ 怎样运行
→ 每一步如何演化
→ 当前完成到哪里
```

## 12. 第一阶段完成标准

当你能独立完成以下事情，就已经掌握了 GitHub 的基础使用：

- 看懂仓库首页的主要信息；
- Clone 一个项目并运行；
- 使用 Git 保存自己的修改；
- 把提交 Push 到 GitHub；
- 使用 README 说明项目；
- 使用 `.gitignore` 排除私人和生成文件；
- 通过 `status` 和 `diff` 检查修改；
- 理解 Star、Clone、Fork 和 Pull Request 的区别；
- 知道密钥不能进入仓库；
- 遇到冲突或异常时先停止并检查，而不是执行破坏性命令。

GitHub 对初学者最重要的意义不是社交数据，而是把学习变成持续积累、能够回顾并可以向别人展示的项目过程。
