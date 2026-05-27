---
标题: 学习仪表盘
标签: [数学, 仪表盘]
创建日期: 2026-05-27
类型: 仪表盘
---

# 📊 学习仪表盘

## 今日待复习

```dataview
TABLE 讲次, 题号, 错因类型, 复习状态
FROM "04_Records/Mistakes"
WHERE 复习状态 = "待重做" OR 复习状态 = "已重做仍错"
SORT 下次复习日期 ASC
```

## 待复习重点题

```dataview
TABLE 讲次, 题号, 复习状态
FROM "04_Records/KeyProblems"
WHERE 复习状态 = "待复习"
SORT 创建日期 ASC
```

## 错题统计（按讲次）

```dataview
TABLE length(rows) AS "错题数"
FROM "04_Records/Mistakes"
GROUP BY 讲次
```

## 错因类型分布

```dataview
TABLE length(rows) AS "题数"
FROM "04_Records/Mistakes"
GROUP BY 错因类型
```

## Wiki 待核查

```dataview
TABLE 类型, 讲次
FROM "03_Wiki"
WHERE AI状态 = "待核查"
SORT 创建日期 DESC
```

## 各讲内容概览

```dataview
TABLE length(rows) AS "页面数"
FROM "03_Wiki"
GROUP BY 所有(file.tags)
```

## 最近学习记录

```dataview
TABLE 讲次, 类型, 创建日期
FROM "02_Learning"
SORT 创建日期 DESC
LIMIT 10
```

## 复习计划

```dataview
TABLE 讲次, 题号, 下次复习日期
FROM "04_Records/Mistakes"
WHERE 下次复习日期 >= date(today)
SORT 下次复习日期 ASC
LIMIT 10
```
