# LangGraph 简单智能体快速入门

一个简单的 LangGraph 智能体快速入门模板，展示了使用 LangGraph 框架构建 AI 智能体的基本结构。

## 特性

- 🚀 **快速开始**: 几分钟内即可开始使用 LangGraph
- 🔧 **模块化设计**: 清晰的关注点分离，包含图、状态、工具和提示词的专用模块
- 🛠️ **工具集成**: 内置示例工具（获取当前时间）
- 🎯 **React 智能体**: 使用 LangGraph 的预构建 React 智能体模式
- 📦 **现代包管理**: 使用 `uv` 进行快速可靠的依赖管理
- 🔑 **灵活的 API 支持**: 兼容 OpenAI API 和 DeepSeek API

## 项目结构

```
src/
├── agent/
│   ├── __init__.py
│   ├── graph.py        # 主要的 LangGraph 图定义
│   ├── state.py        # 智能体状态管理
│   ├── tools.py        # 自定义工具和函数
│   ├── prompts.py      # 系统提示词和模板
│   └── utils.py        # 智能体创建的工具函数
├── langgraph.json      # LangGraph 配置
└── pyproject.toml      # 项目依赖和元数据
```

## 前置要求

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) 包管理器
- OpenAI API 密钥或 DeepSeek API 密钥

## 安装

1. **克隆仓库**
   ```bash
   git clone https://github.com/hfyydd/a_simple_agent_quickstart.git
   cd a_simple_agent_quickstart
   ```

2. **使用 uv 安装依赖**
   ```bash
   uv sync
   ```

3. **设置环境变量**
   ```bash
   # 复制示例环境文件
   cp .env.example .env
   
   # 编辑 .env 并添加你的 API 密钥
   # 对于 OpenAI:
   OPENAI_API_KEY=你的openai_api_密钥
   MODEL_NAME=gpt-4
   
   # 对于 DeepSeek:
   DEEPSEEK_API_KEY=你的deepseek_api_密钥
   DEEPSEEK_BASE_URL=https://api.deepseek.com
   DEEPSEEK_MODEL=deepseek-chat
   ```

## 使用方法

### 开发模式

使用 LangGraph CLI 在开发模式下运行智能体：

```bash
uv run langgraph dev
```

这将启动开发服务器，你可以通过 LangGraph Studio 界面与智能体交互。

### 直接使用

你也可以在 Python 代码中直接使用智能体：

```python
from src.agent.graph import graph

# 运行智能体
result = await graph.ainvoke({
    "messages": [{"role": "user", "content": "现在几点了？"}]
})

print(result["messages"][-1]["content"])
```

## 核心组件

### 1. 状态管理 (`state.py`)
使用 TypedDict 定义智能体的状态结构：
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
```

### 2. 图定义 (`graph.py`)
包含主要的 LangGraph 图，包括：
- 节点定义 (chatbot_node)
- 边连接
- 图编译

### 3. 工具 (`tools.py`)
智能体可用的自定义工具：
- `get_current_time`: 返回当前时间戳

### 4. 提示词 (`prompts.py`)
智能体行为自定义的系统提示词和模板。

### 5. 工具函数 (`utils.py`)
智能体创建和配置的工具函数。

## 自定义

### 添加新工具

1. 在 `src/agent/tools.py` 中定义你的工具：
```python
@tool
def my_custom_tool(input: str) -> str:
    """描述这个工具的功能"""
    # 你的工具逻辑
    return result
```

2. 在 `graph.py` 中导入并添加到工具列表：
```python
from src.agent.tools import get_current_time, my_custom_tool

agent = create_agent("chatbot", llm, [get_current_time, my_custom_tool], system_prompt)
```

### 修改提示词

编辑 `src/agent/prompts.py` 来自定义智能体的行为：
```python
system_prompt = """
你的自定义系统提示词。
定义智能体的角色、能力和行为。
"""
```

### 添加新节点

通过在 `graph.py` 中添加新节点来扩展图：
```python
async def my_new_node(state: State):
    # 你的节点逻辑
    return {"messages": [new_message]}

builder.add_node("my_node", my_new_node)
builder.add_edge("chatbot", "my_node")
```

## API 配置

智能体支持多种 LLM 提供商：

- **OpenAI**: 设置 `OPENAI_API_KEY` 和 `MODEL_NAME`
- **DeepSeek**: 设置 `DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL` 和 `DEEPSEEK_MODEL`
- **其他 OpenAI 兼容的 API**: 相应地配置基础 URL 和 API 密钥

## 贡献

1. Fork 仓库
2. 创建功能分支
3. 进行更改
4. 如适用，添加测试
5. 提交拉取请求

## 许可证

本项目是开源的，遵循 [MIT 许可证](LICENSE)。

## 支持

如果遇到任何问题或有疑问，请：
1. 查看 [LangGraph 文档](https://langchain-ai.github.io/langgraph/)
2. 在此仓库中提出问题
3. 加入 LangChain 社区讨论

## 致谢

- 使用 [LangGraph](https://github.com/langchain-ai/langgraph) 构建
- 包管理由 [uv](https://docs.astral.sh/uv/) 提供
- 兼容 OpenAI 和 DeepSeek API 