# Remote Text Display

一个简单的网页应用，用于展示和轮播文本内容。

## 功能特点

- 从远程GitHub仓库加载文本内容
- 自动轮播显示文本
- 支持全屏显示模式
- 自动横屏适配
- 离线缓存支持
- 定期自动更新内容

## 项目结构

```
remoteTextDisplay/
├── code/
│   └── txtDisplay.html    # 主要应用文件
├── doc/
│   ├── design.md         # 技术设计文档
│   └── api.md           # API参考文档
└── README.md            # 项目说明
```

## 使用方法

1. 直接打开 `code/txtDisplay.html` 文件
2. 点击右下角的全屏按钮可以进入全屏模式
3. 文本内容每5分钟自动从远程更新一次
4. 左下角显示最后更新时间

## 文档

- [技术设计文档](doc/design.md)
- [API参考文档](doc/api.md)
