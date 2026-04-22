# sourceFrom 字段搜索报告

## 搜索结果统计
共找到 17 处使用

### src/services/configManager.js:3
```
this.sourceFrom = 'default';
```

**上下文:**
-   constructor() {
-     this.sourceFrom = 'default';
-   }
- 

### src/services/configManager.js:8
```
this.sourceFrom = source;
```

**上下文:**
-   setSource(source) {
-     this.sourceFrom = source;
-     console.log(`数据源已设置为: ${this.sourceFrom}`);
-   }

### src/services/configManager.js:9
```
console.log(`数据源已设置为: ${this.sourceFrom}`);
```

**上下文:**
-     this.sourceFrom = source;
-     console.log(`数据源已设置为: ${this.sourceFrom}`);
-   }
- 

### src/services/configManager.js:14
```
return this.sourceFrom;
```

**上下文:**
-   getSource() {
-     return this.sourceFrom;
-   }
- 

### src/services/businessLogic.js:8
```
// 检查数据是否包含sourceFrom字段
```

**上下文:**
-     
-     // 检查数据是否包含sourceFrom字段
-     if (data.sourceFrom) {
-       console.log(`数据来源: ${data.sourceFrom}`);

### src/services/businessLogic.js:9
```
if (data.sourceFrom) {
```

**上下文:**
-     // 检查数据是否包含sourceFrom字段
-     if (data.sourceFrom) {
-       console.log(`数据来源: ${data.sourceFrom}`);
-       return this.enhanceData(data);

### src/services/businessLogic.js:10
```
console.log(`数据来源: ${data.sourceFrom}`);
```

**上下文:**
-     if (data.sourceFrom) {
-       console.log(`数据来源: ${data.sourceFrom}`);
-       return this.enhanceData(data);
-     } else {

### src/services/businessLogic.js:13
```
console.log('数据缺少sourceFrom字段');
```

**上下文:**
-     } else {
-       console.log('数据缺少sourceFrom字段');
-       return { ...data, error: '数据缺少来源信息' };
-     }

### src/services/businessLogic.js:21
```
switch (data.sourceFrom) {
```

**上下文:**
-     // 根据不同的数据源进行不同的处理
-     switch (data.sourceFrom) {
-       case 'database':
-         return this.enhanceDatabaseData(data);

### src/services/dataService.js:5
```
this.sourceFrom = null;
```

**上下文:**
-   constructor() {
-     this.sourceFrom = null;
-   }
- 

### src/services/dataService.js:11
```
this.sourceFrom = configManager.getSource();
```

**上下文:**
-     // 从配置管理器获取数据源
-     this.sourceFrom = configManager.getSource();
-     
-     console.log(`从 ${this.sourceFrom} 获取数据`);

### src/services/dataService.js:13
```
console.log(`从 ${this.sourceFrom} 获取数据`);
```

**上下文:**
-     
-     console.log(`从 ${this.sourceFrom} 获取数据`);
-     
-     // 根据不同的数据源返回不同的数据

### src/services/dataService.js:16
```
switch (this.sourceFrom) {
```

**上下文:**
-     // 根据不同的数据源返回不同的数据
-     switch (this.sourceFrom) {
-       case 'database':
-         return this.fetchFromDatabase();

### src/services/dataService.js:33
```
sourceFrom: this.sourceFrom
```

**上下文:**
-       name: '数据库数据',
-       sourceFrom: this.sourceFrom
-     };
-   }

### src/services/dataService.js:42
```
sourceFrom: this.sourceFrom
```

**上下文:**
-       name: 'API数据',
-       sourceFrom: this.sourceFrom
-     };
-   }

### src/services/dataService.js:51
```
sourceFrom: this.sourceFrom
```

**上下文:**
-       name: '文件数据',
-       sourceFrom: this.sourceFrom
-     };
-   }

### src/services/dataService.js:57
```
return this.sourceFrom;
```

**上下文:**
-   getSourceFrom() {
-     return this.sourceFrom;
-   }
- }

