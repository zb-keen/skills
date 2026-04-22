const dataService = require('./dataService');

class BusinessLogic {
  // 处理数据
  processData(data) {
    console.log('处理数据:', data);
    
    // 检查数据是否包含sourceFrom字段
    if (data.sourceFrom) {
      console.log(`数据来源: ${data.sourceFrom}`);
      return this.enhanceData(data);
    } else {
      console.log('数据缺少sourceFrom字段');
      return { ...data, error: '数据缺少来源信息' };
    }
  }

  // 增强数据
  enhanceData(data) {
    // 根据不同的数据源进行不同的处理
    switch (data.sourceFrom) {
      case 'database':
        return this.enhanceDatabaseData(data);
      case 'api':
        return this.enhanceApiData(data);
      case 'file':
        return this.enhanceFileData(data);
      default:
        return data;
    }
  }

  // 增强数据库数据
  enhanceDatabaseData(data) {
    return {
      ...data,
      processed: true,
      databaseSpecific: '数据库特定处理'
    };
  }

  // 增强API数据
  enhanceApiData(data) {
    return {
      ...data,
      processed: true,
      apiSpecific: 'API特定处理'
    };
  }

  // 增强文件数据
  enhanceFileData(data) {
    return {
      ...data,
      processed: true,
      fileSpecific: '文件特定处理'
    };
  }

  // 同步数据源
  syncSource(source) {
    console.log(`同步数据源到: ${source}`);
    // 这里可以添加同步逻辑
  }
}

module.exports = new BusinessLogic();
