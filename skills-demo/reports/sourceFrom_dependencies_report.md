# sourceFrom 字段依赖分析报告

## 字段相关依赖关系图

```mermaid
graph TD
    src_services_businessLogic_js[src/services/businessLogic.js] --> __dataService[./dataService]
    src_services_dataService_js[src/services/dataService.js] --> __configManager[./configManager]
```

## 详细依赖列表

### src/services/businessLogic.js
- const dataService = require('./dataService');

### src/services/dataService.js
- const configManager = require('./configManager');

