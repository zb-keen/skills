// 主应用文件
const Config = require('./config');

const App = {
  sourceFrom: Config.getSource(),
  
  init() {
    console.log('App initialized with sourceFrom:', this.sourceFrom);
    this.loadData();
  },
  
  loadData() {
    if (this.sourceFrom === 'local') {
      this.loadLocalData();
    } else if (this.sourceFrom === 'api') {
      this.loadApiData();
    }
  },
  
  loadLocalData() {
    console.log('Loading data from local storage');
  },
  
  loadApiData() {
    console.log('Loading data from API');
  },
  
  updateSource(source) {
    this.sourceFrom = source;
    Config.setSource(source);
    console.log('Updated sourceFrom to:', this.sourceFrom);
  }
};

App.init();

// 模拟运行时更新
setTimeout(() => {
  App.updateSource('api');
  App.loadData();
}, 1000);
