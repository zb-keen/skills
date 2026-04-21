# sourceFrom 字段使用模式分析报告

## 注意事项

本分析基于规则对使用场景进行分类，可能不完全准确。
建议结合实际代码进行验证。

## 可能的assignment场景 (1 处)

### src/main.js:29
```
this.sourceFrom = source;
```

## 可能的usage场景 (3 处)

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

## 可能的condition场景 (2 处)

### src/main.js:13
```
if (this.sourceFrom === 'local') {
```

### src/main.js:15
```
} else if (this.sourceFrom === 'api') {
```

## 使用文件统计

字段在 1 个文件中被找到

- src/main.js
