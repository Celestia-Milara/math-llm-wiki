# 考研数学提分系统 (Score-Boosting Engine) 架构手册 v2.0

## 一、 目录全景图 (Vault Structure)

```
.
├── 00_Raw/                  # 原始素材层（只读燃料）
│   ├── Lectures/            # 《30讲》Markdown 全文
│   ├── Problems/            # 《1000题》题干及解析 Markdown
│   ├── Images/              # 原始图片素材（命名：文件名_001.png）
│   └── Archive/             # 已处理素材归档区
├── 01_Wiki/                 # 结构化知识层（核心引擎）
│   ├── Concepts/            # 概念库：定义、核心思想
│   ├── Theorems/            # 定理库：性质、推论
│   ├── Chains/              # 推导链：逻辑演变过程（Why）
│   ├── Methods/             # 方法库：解题 SOP（How / 提分核心）
│   └── Problems/            # 题目索引库：题目履历与得分状态
├── 02_Output/               # 仪表盘层（数据输出）
│   ├── Weakness_Report.md   # 弱点诊断报告
│   └── Review_List.md       # 动态复习清单
├── 03_Daily/                # 指令层（交互中心）
│   └── YYYY-MM-DD.md        # 每日学习日志（系统触发器）
├── 04_Templates/            # 规范层（元数据基因）
│   ├── Concept_Template.md
│   ├── Theorem_Template.md
│   ├── Method_Template.md
│   ├── Problem_Template.md
│   └── Daily_Template.md
└── claude.md                # AI 管理员手册（运行逻辑定义）
```

## 二、 文件夹详解与维护策略

### 1. 00_Raw (原始素材层)

- **存放内容**：由用户预处理好的 Markdown 文件。
    
- **图片管理**：所有 MD 引用的图片统一存放在 `00_Raw/Images/`。
    
    - **命名规则**：`[对应文件名]_[序号]`（如：`张宇30讲_01_001.png`）。
        
- **归档机制**：AI 处理完一个 MD 后，必须将其连同修改后的 Frontmatter 移至 `00_Raw/Archive/`，确保 `Lectures/` 和 `Problems/` 目录只包含“待处理”的新内容。
    

### 2. 01_Wiki/Methods (方法库 - **系统灵魂**)

- **功能**：存放解题算法（SOP）。
    
- **来源**：
    
    - **AI 提取**：从 Lectures 或错题解析中自动抽象。
        
    - **手动录入**：用户在备考过程中记录的高质量第三方解法。
        
- **错误反馈逻辑**：
    
    - `Method` 页面保留 `## 避坑指南 (Anti-Patterns)` 章节。
        
    - 当 `Daily` 产生错题反馈时，AI 会将该错误抽象成一条“动作指令”更新到此处。
        

### 3. 01_Wiki/Problems (题目索引库)

- **功能**：单题的“电子病历”。
    
- **内容**：不重复存储题干，仅记录 `题目状态`、`我的错因`、`关联方法`。
    
- **维护**：由 AI 根据日记自动更新。
    

### 4. 04_Templates (规范层)

- **功能**：强制约束所有 Wiki 页面的 Frontmatter（元数据），这是 Dataview 正常工作的保障。
    
- **核心模板列表**：
    
    - `Method_Template.md`: 必须包含 `applicable_when`, `steps`, `error_prone_points`。
        
    - `Problem_Template.md`: 必须包含 `status`, `mistake_type`, `related_methods`。
        

## 三、 核心运行流 (Data Flow)

### 1. 原始素材归档流 (Processing & Archiving)

- **输入**：用户将预处理好的 MD 放入 `00_Raw/Lectures/`。
    
- **动作**：AI 读取 -> 提取原子笔记写入 `01_Wiki` -> 在原 MD 添加 `processed_at` 标签 -> 移入 `00_Raw/Archive/`。
    

### 2. 日记驱动分析流 (Daily Feedback Loop)

- **触发**：用户在日记中标记 `- [!] [[Problem_123]]` 并写下简短错因。
    
- **AI 动作**：
    
    1. 检索 `00_Raw/Problems/` 中编号为 123 的解析。
        
    2. 更新 `01_Wiki/Problems/Problem_123.md` 的错误记录。
        
    3. **方法补丁**：将错因抽象化，更新到关联的 `Method` 页面中。
        

## 四、 文件夹维护职责划分

|角色|维护文件夹|维护频率|
|---|---|---|
|**用户 (You)**|`00_Raw/` (放入新 MD), `03_Daily/` (写日记), `01_Wiki/Methods` (手动补充)|每日|
|**AI (Claude)**|`01_Wiki/` (创建/更新), `00_Raw/Archive/` (归档), `02_Output/` (更新报告)|触发式|
|**系统 (Obsidian)**|`04_Templates/` (提供格式指导)|静态|

## 五、 设计原则：为何如此分工？

1. **图片可追溯**：强制命名规则确保在数千张图片中，依然能一眼看出图片属于哪道题。
    
2. **方法大于题目**：虽然错题触发系统，但最终成果必须沉淀在 `Methods` 中，实现“做一题会一类”。
    
3. **确定性归档**：归档机制解决了 AI 重复扫描的问题，极大节省了 Context。