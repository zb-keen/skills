const dataService = require('./services/dataService');
const businessLogic = require('./services/businessLogic');
const configManager = require('./services/configManager');

// 初始化应用
function initApp() {
  console.log('初始化应用...');
  
  // 设置数据源
  configManager.setSource('database');
  
  // 获取数据
  const data = dataService.getData();
  console.log('获取的数据:', data);
  
  // 处理数据
  const processedData = businessLogic.processData(data);
  console.log('处理后的数据:', processedData);
}

// 运行应用
initApp();
