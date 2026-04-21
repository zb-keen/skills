# sourceFrom 字段搜索报告

## 搜索结果统计
共找到 6 处使用

### src/main.js:5
```
sourceFrom: Config.getSource(),
```

**上下文:**
- const App = {
-   sourceFrom: Config.getSource(),
-   
-   init() {

### src/main.js:8
```
console.log('App initialized with sourceFrom:', this.sourceFrom);
```

**上下文:**
-   init() {
-     console.log('App initialized with sourceFrom:', this.sourceFrom);
-     this.loadData();
-   },

### src/main.js:13
```
if (this.sourceFrom === 'local') {
```

**上下文:**
-   loadData() {
-     if (this.sourceFrom === 'local') {
-       this.loadLocalData();
-     } else if (this.sourceFrom === 'api') {

### src/main.js:15
```
} else if (this.sourceFrom === 'api') {
```

**上下文:**
-       this.loadLocalData();
-     } else if (this.sourceFrom === 'api') {
-       this.loadApiData();
-     }

### src/main.js:29
```
this.sourceFrom = source;
```

**上下文:**
-   updateSource(source) {
-     this.sourceFrom = source;
-     Config.setSource(source);
-     console.log('Updated sourceFrom to:', this.sourceFrom);

### src/main.js:31
```
console.log('Updated sourceFrom to:', this.sourceFrom);
```

**上下文:**
-     Config.setSource(source);
-     console.log('Updated sourceFrom to:', this.sourceFrom);
-   }
- };

