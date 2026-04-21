# 代码依赖分析报告

## 依赖关系图

```mermaid
graph TD
    src_main_js[src/main.js] --> __config[./config]
```

## 详细依赖列表

### src/main.js
- const Config = require('./config');

