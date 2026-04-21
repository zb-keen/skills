# sourceFrom 字段逻辑分析报告

## assignment (3 处)

### src/main.js:13
```
if (this.sourceFrom === 'local') {
```

### src/main.js:15
```
} else if (this.sourceFrom === 'api') {
```

### src/main.js:29
```
this.sourceFrom = source;
```

## usage (3 处)

### src/main.js:5
```
sourceFrom: Config.getSource(),
```

### src/main.js:8
```
console.log('App initialized with sourceFrom:', this.sourceFrom);
```

### src/main.js:31
```
console.log('Updated sourceFrom to:', this.sourceFrom);
```

## 影响范围分析

字段在 1 个文件中使用

- src/main.js
