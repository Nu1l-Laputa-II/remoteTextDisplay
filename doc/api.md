# API 参考文档

## 数据源API

### GitHub Raw Content
- **终端点**: `https://raw.githubusercontent.com/Nu1l-Laputa-II/goldenSentence/main/sentence.md`
- **方法**: GET
- **响应格式**: 纯文本
- **更新频率**: 5分钟
- **错误处理**: 最多重试3次

## 核心功能API

### 数据获取
```javascript
async function fetchSentences()
```
- 功能：获取远程文本内容
- 参数：无
- 返回：void
- 异常处理：网络错误时使用缓存

### 文本展示
```javascript
function displayText()
```
- 功能：控制文本显示和动画
- 参数：无
- 返回：void
- 动画时长：2秒过渡

### 初始化
```javascript
async function init()
```
- 功能：程序初始化
- 参数：无
- 返回：void
- 行为：加载缓存、首次获取数据

## 浏览器API使用

### 存储API
- LocalStorage
  - cachedSentences: 句子缓存
  - lastUpdateTime: 更新时间

### 显示API
- Fullscreen API
- Screen Orientation API

## DOM元素

### 关键元素ID
- text-container: 文本容器
- update-time: 更新时间显示
- fullscreen-btn: 全屏控制
