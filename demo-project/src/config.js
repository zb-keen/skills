// 配置文件
const Config = {
  defaultSource: 'local',
  
  getSource() {
    return this.defaultSource;
  },
  
  setSource(source) {
    this.defaultSource = source;
  }
};

// 导出配置
module.exports = Config;
