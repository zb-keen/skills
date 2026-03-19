# Keen Skills / 敏锐技能集

A collection of AI-powered skills for enhancing conversation management and question optimization.

用于增强对话管理和问题优化的 AI 技能集合。

---

## 📋 Overview / 概述

Keen Skills is a modular skill system designed to improve AI assistant capabilities in handling complex conversations and optimizing user queries.

Keen Skills 是一个模块化技能系统，旨在提升 AI 助手处理复杂对话和优化用户查询的能力。

---

## 🗂️ Project Structure / 项目结构

```
keen-skills/
├── conversation-manager/          # 对话管理技能
│   ├── SKILL.md                   # Skill definition / 技能定义
│   ├── compression/               # Compressed conversation storage / 压缩对话存储
│   ├── scripts/                   # Python automation scripts / Python 自动化脚本
│   │   ├── get_timestamp.py       # Timestamp generation / 时间戳生成
│   │   ├── topic_detection.py     # Topic clustering / 主题聚类
│   │   ├── hybrid_retrieval.py    # Hybrid search / 混合检索
│   │   ├── storage_management.py  # Storage cleanup / 存储清理
│   │   └── main.py                # Main entry point / 主入口
│   └── topic/                     # Topic-based memory / 主题记忆
│
├── question-optimizer/            # 问题优化技能
│   └── SKILL.md                   # Skill definition / 技能定义
│
└── README.md                      # This file / 本文件
```

---

## 🎯 Skills / 技能

### 1. Conversation Manager / 对话管理器

**Purpose / 用途**: Manage long conversations with compression, topic segmentation, and hybrid retrieval.

管理长对话，提供会话压缩、主题分割和混合检索功能。

**Features / 功能特点**:

| Feature | Description | 功能 | 描述 |
|---------|-------------|------|------|
| Session Compression | Auto-compress long conversations while preserving context | 会话压缩 | 自动压缩长对话，在保持上下文的同时减少内存使用 |
| Topic Segmentation | Classify conversations by topics using TF-IDF and K-means | 主题分割 | 使用 TF-IDF 和 K-means 算法按主题分类对话 |
| Hybrid Retrieval | Combine keyword (70%) and semantic (30%) search | 混合检索 | 结合关键词检索(70%)和语义检索(30%) |
| Storage Management | Auto-cleanup files older than 30 days | 存储管理 | 自动清理超过30天的文件 |

**Scripts / 脚本**:
- `get_timestamp.py` - Generate precise timestamps for file naming / 生成精确时间戳用于文件命名
- `topic_detection.py` - Intelligent topic clustering / 智能主题聚类
- `hybrid_retrieval.py` - Hybrid search implementation / 混合检索实现
- `storage_management.py` - Storage statistics and cleanup / 存储统计和清理

---

### 2. Question Optimizer / 问题优化器

**Purpose / 用途**: Optimize user questions before answering to ensure precise responses.

在回答之前优化用户问题，确保提供精准的回答。

**Workflow / 工作流程**:
1. **Receive Question / 接收问题** - Accept user's original question / 接受用户的原始问题
2. **Analyze & Optimize / 分析优化** - Identify ambiguities and generate 2-3 refined versions / 识别模糊点并生成2-3个优化版本
3. **Request Confirmation / 请求确认** - Present options and ask user to choose / 呈现选项并请用户选择
4. **Answer / 回答** - Provide detailed response based on confirmed version / 基于确认的版本提供详细回答

**Key Rule / 核心规则**: Never answer directly before optimization and user confirmation.

**核心规则**: 在优化并获取用户确认之前，绝不直接回答。

---

## 🚀 Usage / 使用方法

### Conversation Manager / 对话管理器

```python
# Run the conversation manager
python conversation-manager/scripts/main.py

# Individual scripts / 独立脚本
python conversation-manager/scripts/topic_detection.py
python conversation-manager/scripts/hybrid_retrieval.py
python conversation-manager/scripts/storage_management.py
```

### Question Optimizer / 问题优化器

This skill is automatically applied to all user inputs. No manual activation needed.

此技能自动应用于所有用户输入，无需手动激活。

---

## 🛠️ Requirements / 环境要求

- Python 3.8+
- Dependencies / 依赖项:
  - scikit-learn (for TF-IDF and K-means / 用于 TF-IDF 和 K-means)
  - numpy
  - pandas

---

## 📁 Storage Locations / 存储位置

- **Compression Files / 压缩文件**: `conversation-manager/compression/YYYY_MM_DD_HH_MM_SS.md`
- **Topic Files / 主题文件**: `conversation-manager/topic/主题_*.md`

---

## 🤝 Contributing / 贡献

1. Fork the repository / 复刻仓库
2. Create a new skill directory / 创建新的技能目录
3. Add SKILL.md with definition / 添加包含定义文件的 SKILL.md
4. Submit a pull request / 提交拉取请求

---

## 📝 License / 许可证

MIT License - See LICENSE file for details.

MIT 许可证 - 详情请参阅 LICENSE 文件。

---

## 🔗 Related / 相关

- [Trae IDE](https://trae.ai/) - The AI-powered IDE for this project / 本项目使用的 AI 驱动 IDE
- [MCP Protocol](https://modelcontextprotocol.io/) - Model Context Protocol / 模型上下文协议

---

<p align="center">
  <strong>Keen Skills - Making AI Conversations Smarter</strong><br>
  <strong>敏锐技能集 - 让 AI 对话更智能</strong>
</p>
