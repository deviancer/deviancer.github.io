# Deviancer Blog 项目注意事项

## 仓库结构

```
deviancer.github.io/          # 公开仓库（GitHub Pages）
├── shop-timer/              # submodule → deviancer/shop-timer (公开)
├── gitadora_nine_grid/      # submodule → deviancer/gitadora_nine_grid (公开)
└── ...

blog-src/                    # 私有仓库（源码备份）
└── (完整代码副本)
```

## 子项目更新流程

当 `shop-timer` 或 `gitadora_nine_grid` 有更新时：

```bash
# 1. 在子项目目录中
cd shop-timer  # 或 gitadora_nine_grid

# 2. 拉取最新代码
git pull origin main

# 3. 返回主仓库
cd ..

# 4. 更新submodule引用
git add shop-timer gitadora_nine_grid
git commit -m "chore: 更新子项目"
git push origin main
```

## 写作规范

文章frontmatter格式：

```yaml
---
layout: post
title: "标题"
date: 2024-01-01          # 首次发布日期
updated: 2024-01-02       # 最新更新日期（可选，如果没有更新则为空）
tags: 标签1, 标签2        # 标签，可多个
categories: 分类          # 分类
---
```

## 私有仓库

- 公开仓库: https://github.com/deviancer/deviancer.github.io
- 私有备份: https://github.com/deviancer/blog-src (private)

## 注意事项

1. submodule需要确保子项目仓库是公开的，否则GitHub Pages无法访问
2. 更新子项目后一定要在主仓库commit并push，否则页面不会更新
3. 如果需要在本地预览，需要初始化submodule: `git submodule update --init --recursive`