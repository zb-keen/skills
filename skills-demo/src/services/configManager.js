class ConfigManager {
  constructor() {
    this.sourceFrom = 'default';
  }

  // 设置数据源
  setSource(source) {
    this.sourceFrom = source;
    console.log(`数据源已设置为: ${this.sourceFrom}`);
  }

  // 获取数据源
  getSource() {
    return this.sourceFrom;
  }

  // 验证数据源
  validateSource(source) {
    const validSources = ['database', 'api', 'file'];
    return validSources.includes(source);
  }

  // 获取默认数据源
  getDefaultSource() {
    return 'database';
  }
}

module.exports = new ConfigManager();
