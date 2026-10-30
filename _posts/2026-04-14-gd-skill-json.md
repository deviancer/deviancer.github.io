---
layout: post
title: "使用 GD_skill 生成器获取所需 JSON 的方法"
date: 2026-04-14
updated:
tags: gitadora
categories: 技术
---

## 操作步骤

> https://gd-scoretable.onrender.com/

### 1. 导入 JSON 帮助文件

点击右上角的 **导入**，依次选择 **导入 JSON** 和 **JSON 帮助**。

![json1.png](/assets/images/json1.png)
![json2.png](/assets/images/json2.png)
![json3.png](/assets/images/json3.png)

### 2. 复制 JSON 数据

复制你的skill，只要有文本就行。电脑端随便拉一下复制就行.jpg

### 3. 使用 AI 转换数据

请参考以下提示词与 JSON 模板，将你的数据交给 AI 处理：

> 帮我将以下数据转换为这个标准 JSON 文件中的 `entries` 字段。


```json
{
  "player_name": "你的名字",
  "mode": "DM",            // DM 或 GF
  "version": "gwd",        // gw 或 gwd
  "entries": [
    {
      "song_title": "I think about you",    // 歌曲名称
      "sheet_type": "drum",                 // drum, guitar, bass
      "sheet_difficulty": "extreme",        // basic, advanced, extreme, master
      "level_value": 5.85,                  // 难度等级
      "achievement": 99.81,                 // 达成率 (%)
      "skill_point": 116.77                 // Skill 点数
    }
  ]
}
```

#### 示例截图

![我的分1.png](/assets/images/我的分1.png)
![我的分2.png](/assets/images/我的分2.png)
![豆包](/assets/images/豆包.png)

### 4. 将 AI 转换后的 JSON 写回

将 AI 返回的正确 JSON 内容复制回生成器对应位置。

![记得改.png](/assets/images/记得改.png)

### 5. 完成

恭喜，现在你检查一下内容是否ok就行，也可以点击右上角的检验skill看看，然后就可以生成图片了！

---

## 更新日志

- **V1.0**  
  本地测试生成 Skill 图片，手动添加数据，读取并保存 JSON。

- **V2.0**  
  通过 Render 将 Python 后端 API 部署至网页。

- **V2.1**  
  - 修复手机端导入按钮显示问题  
  - 修复 gw 与 gwd 版本 hot 共同曲显示问题  
  - 优化 UI：增加每页显示歌曲数量及跨页功能  
  - 增加中/英/日文切换按钮

- **V2.2**  
  - 简化 JSON 导入与导出内容  
  - 增加校验 Skill 按钮（不强制校验，但请勿作弊）  
  - 增加清理数据按钮  
  - 修改颜色命名：“红” → “赤”

- **V2.3** 
  - 添加了 GSV 的友情链接和介绍
  - 更改了难度显示框，更符合游戏
  - 添加了 ❓ 按钮，里面有更新日志和意见邮箱
  - 在歌曲详细信息中添加了 BPM 显示
  - 在歌曲详细信息中添加了初出版本和存续版本
  - 现在可以搜索作者了，包括作者的罗马音
  - TODO：某些含有变化 BPM 的还得修`;

```
有问题找我，怎么找我？你知道的^^