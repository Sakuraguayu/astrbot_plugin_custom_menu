</div>

<div align="center">

![:name](https://count.getloli.com/@astrbot_plugin_custom_menu?name=astrbot_plugin_custom_menu&theme=minecraft&padding=7&offset=0&align=top&scale=1&pixelated=1&darkmode=auto)

</div>

# astrbot_plugin_custom_menu

[仅QQ] 一个适用于 AstrBot 的自定义图片菜单插件。

用户只需要将菜单图片放入 `menu` 文件夹，即可通过指令快速发送菜单图片。

当前版本已修改为：

- 不再使用合并转发
- 直接发送图片
- 随机发送菜单图片
- 更适合二次元 Bot / QQ Bot 使用场景

---

# 功能特性

- 支持图片格式：
  - `jpg`
  - `jpeg`
  - `png`
  - `gif`
  - `bmp`
  - `webp`

- 自动检测 `menu` 文件夹中的图片

- 支持多个菜单指令：
  - `菜单`
  - `帮助`
  - `功能`
  - `你怎么用`

- 随机发送菜单图片

- 自动创建 `menu` 文件夹

- 直接发送图片而不是合并转发

---

# 使用方法

## 1. 安装插件

将插件放入 AstrBot 插件目录。

---

## 2. 放入菜单图片

首次运行插件后，会自动创建：

```text
menu/
```

将你的菜单图片放入该目录即可。

例如：

```text
menu/
├── menu1.png
├── menu2.jpg
├── help.webp
└── anime_menu.png
```

---

## 3. 使用菜单指令

在 QQ 中发送：

```text
菜单
```

或：

```text
帮助
功能
你怎么用
```

Bot 会随机发送一张菜单图片。

---

# 更新日志

## 1.0.0

- 初版自定义菜单
- 使用合并转发发送图片

## 2.0.0

- 每张图片单独发送
- 减少消息阅读压力

## 3.0.0

- 改为直接发送图片
- 不再使用合并转发
- 支持随机菜单
- 支持 `webp`
- 更适合 QQ 二次元 Bot

---

# 注意事项

- 更新插件前请备份 `menu` 文件夹
- 图片过大会被 QQ 压缩
- gif 动图受 QQ 限制可能无法完整播放
- 建议菜单图片宽度不要超过 `1920px`

---

# 分支说明

当前版本为修改版分支。

相较于原版：

- 修改了菜单发送逻辑
- 优化了 QQ 阅读体验
- 更适合高颜值 Bot 菜单

---

# 致谢

原项目作者：Futureppo
修改版维护：Sakurayu
