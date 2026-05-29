# 考研数学 LLM Wiki

> An Obsidian-based knowledge management system for postgraduate math exam preparation, powered by Claude Code and DeepSeek API.

这是一个基于 Obsidian 的考研数学 LLM 辅助学习闭环系统。它不只是数学资料仓库，而是将学习、做题、纠错、复习串联成完整闭环的智能 Wiki。

---

## 核心理念

传统笔记是静态的，这个系统是动态的：

- **学习前** — 生成行动型学习指南，告诉你怎么学、怎么做题、怎么自查
- **做题后** — 分析错题和重点题，优先分析**你自己的错误思路**，而非只给标准答案
- **理解时** — 审查你的概念复述，指出会导致做题错误的风险
- **沉淀后** — 将长期有价值的内容写入 Wiki、记录复习计划

## 学习闭环

```
学习指南 -> 做题记录 -> 错题/重点题 Records
-> 错因分析 -> Wiki/题型/方法补充
-> 概念理解审查 -> 复习计划
```

## 目录结构

```
math/
├── 00_Inbox/          临时输入
├── 01_Raw/            原始资料（讲义、题目、图片）
├── 02_Learning/       学习过程（指南、日记、会话）
├── 03_Wiki/           永久知识库
│   ├── Concepts/      核心概念
│   ├── Theorems/      定理与公式
│   ├── Methods/       解题方法
│   ├── ProblemTypes/  题型分类
│   └── Hubs/          章节索引
├── 04_Records/        错题、重点题、概念审查记录
├── 05_Outputs/        汇总报告（弱点分析、复习计划）
├── 06_Templates/      Obsidian 模板
├── 99_System/         系统规则、提示词、字段规范、脚本
├── .claude/           Claude Code skills 配置
└── CLAUDE.md          LLM 工作协议
```

## 技术栈

| 工具 | 用途 |
|---|---|
| [Obsidian](https://obsidian.md) | 知识管理、Markdown 编辑、双链笔记 |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | 工作环境与文件编排器，负责读写 Obsidian 文件 |
| [DeepSeek API](https://platform.deepseek.com) | 数学推理模型，生成解释、推导、错因分析 |
| [Git LFS](https://git-lfs.github.com) | 管理讲义/题目截图等大文件 |

### 使用的 Obsidian 插件

- **Dataview** — 查询和聚合笔记数据
- **Templater** — 高级模板引擎
- **Obsidian Style Settings** — 主题自定义
- **Obsidian Git** — Git 集成

## 使用方法

### 1. 克隆仓库

```bash
git clone https://github.com/Celestia-Milara/math-llm-wiki
```

> 注意：由于使用了 Git LFS，需要先安装 [Git LFS](https://git-lfs.github.com)：
> ```bash
> git lfs install
> ```

### 2. 用 Obsidian 打开

在 Obsidian 中打开 `math` 文件夹作为 Vault。插件会在首次打开时自动从 Community Plugins 安装。

### 3. 与 Claude Code 配合使用

在 `math` 目录下启动 Claude Code，它会读取 `CLAUDE.md` 中的工作协议，自动按照闭环流程工作：

- 说 "学习第 N 讲" — 生成学习指南
- 记录做题情况 — 分析错题和错误思路
- 复述概念 — 审查理解准确性

## AI 状态说明

本系统中由 AI 生成但未经人工核查的内容会标注 `AI状态: 待核查`，提醒用户需要自行验证。

## License

MIT
