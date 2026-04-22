const configManager = require('./configManager');

class DataService {
  constructor() {
    this.sourceFrom = null;
  }

  // 获取数据
  getData() {
    // 从配置管理器获取数据源
    this.sourceFrom = configManager.getSource();
    
    console.log(`从 ${this.sourceFrom} 获取数据`);
    
    // 根据不同的数据源返回不同的数据
    switch (this.sourceFrom) {
      case 'database':
        return this.fetchFromDatabase();
      case 'api':
        return this.fetchFromApi();
      case 'file':
        return this.fetchFromFile();
      default:
        return { error: '未知数据源' };
    }
  }

  // 从数据库获取数据
  fetchFromDatabase() {
    return {
      id: 1,
      name: '数据库数据',
      sourceFrom: this.sourceFrom
    };
  }

  // 从API获取数据
  fetchFromApi() {
    return {
      id: 2,
      name: 'API数据',
      sourceFrom: this.sourceFrom
    };
  }

  // 从文件获取数据
  fetchFromFile() {
    return {
      id: 3,
      name: '文件数据',
      sourceFrom: this.sourceFrom
    };
  }

  // 获取当前数据源
  getSourceFrom() {
    return this.sourceFrom;
  }
}

module.exports = new DataService();
