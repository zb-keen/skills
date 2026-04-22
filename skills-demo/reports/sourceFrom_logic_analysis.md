# sourceFrom 字段使用模式分析报告

## 注意事项

本分析基于规则对使用场景进行分类，可能不完全准确。
建议结合实际代码进行验证。

## 可能的assignment场景 (4 处)

### src/services/configManager.js:3
```
this.sourceFrom = 'default';
```

### src/services/configManager.js:8
```
this.sourceFrom = source;
```

### src/services/dataService.js:5
```
this.sourceFrom = null;
```

### src/services/dataService.js:11
```
this.sourceFrom = configManager.getSource();
```

## 可能的usage场景 (10 处)

### src/services/configManager.js:9
```
console.log(`数据源已设置为: ${this.sourceFrom}`);
```

### src/services/configManager.js:14
```
return this.sourceFrom;
```

### src/services/businessLogic.js:8
```
// 检查数据是否包含sourceFrom字段
```

### src/services/businessLogic.js:10
```
console.log(`数据来源: ${data.sourceFrom}`);
```

### src/services/businessLogic.js:13
```
console.log('数据缺少sourceFrom字段');
```

### src/services/dataService.js:13
```
console.log(`从 ${this.sourceFrom} 获取数据`);
```

### src/services/dataService.js:33
```
sourceFrom: this.sourceFrom
```

### src/services/dataService.js:42
```
sourceFrom: this.sourceFrom
```

### src/services/dataService.js:51
```
sourceFrom: this.sourceFrom
```

### src/services/dataService.js:57
```
return this.sourceFrom;
```

## 可能的condition场景 (3 处)

### src/services/businessLogic.js:9
```
if (data.sourceFrom) {
```

### src/services/businessLogic.js:21
```
switch (data.sourceFrom) {
```

### src/services/dataService.js:16
```
switch (this.sourceFrom) {
```

## 使用文件统计

字段在 3 个文件中被找到

- src/services/dataService.js
- src/services/configManager.js
- src/services/businessLogic.js
