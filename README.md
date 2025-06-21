# LangGraph Simple Agent Quickstart

A simple LangGraph agent quickstart template that demonstrates the basic structure of building an AI agent with LangGraph framework.

## Features

- 🚀 **Quick Start**: Get started with LangGraph in minutes
- 🔧 **Modular Design**: Clean separation of concerns with dedicated modules for graph, state, tools, and prompts
- 🛠️ **Tool Integration**: Built-in example tools (current time getter)
- 🎯 **React Agent**: Uses LangGraph's prebuilt React agent pattern
- 📦 **Modern Package Management**: Uses `uv` for fast and reliable dependency management
- 🔑 **Flexible API Support**: Compatible with OpenAI API and DeepSeek API

## Project Structure

```
src/
├── agent/
│   ├── __init__.py
│   ├── graph.py        # Main LangGraph graph definition
│   ├── state.py        # Agent state management
│   ├── tools.py        # Custom tools and functions
│   ├── prompts.py      # System prompts and templates
│   └── utils.py        # Utility functions for agent creation
├── langgraph.json      # LangGraph configuration
└── pyproject.toml      # Project dependencies and metadata
```

## Prerequisites

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key or DeepSeek API key

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/hfyydd/a_simple_agent_quickstart.git
   cd a_simple_agent_quickstart
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your API keys
   # For OpenAI:
   OPENAI_API_KEY=your_openai_api_key_here
   MODEL_NAME=gpt-4
   
   # For DeepSeek:
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   DEEPSEEK_BASE_URL=https://api.deepseek.com
   DEEPSEEK_MODEL=deepseek-chat
   ```

## Usage

### Development Mode

Run the agent in development mode with LangGraph CLI:

```bash
uv run langgraph dev
```

This will start the development server and you can interact with your agent through the LangGraph Studio interface.

### Direct Usage

You can also use the agent directly in your Python code:

```python
from src.agent.graph import graph

# Run the agent
result = await graph.ainvoke({
    "messages": [{"role": "user", "content": "What time is it?"}]
})

print(result["messages"][-1]["content"])
```

## Core Components

### 1. State Management (`state.py`)
Defines the agent's state structure using TypedDict:
```python
class State(TypedDict):
    messages: Annotated[list, add_messages]
```

### 2. Graph Definition (`graph.py`)
Contains the main LangGraph graph with:
- Node definitions (chatbot_node)
- Edge connections
- Graph compilation

### 3. Tools (`tools.py`)
Custom tools available to the agent:
- `get_current_time`: Returns current timestamp

### 4. Prompts (`prompts.py`)
System prompts and templates for agent behavior customization.

### 5. Utils (`utils.py`)
Utility functions for agent creation and configuration.

## Customization

### Adding New Tools

1. Define your tool in `src/agent/tools.py`:
```python
@tool
def my_custom_tool(input: str) -> str:
    """Description of what this tool does"""
    # Your tool logic here
    return result
```

2. Import and add it to the tools list in `graph.py`:
```python
from src.agent.tools import get_current_time, my_custom_tool

agent = create_agent("chatbot", llm, [get_current_time, my_custom_tool], system_prompt)
```

### Modifying Prompts

Edit `src/agent/prompts.py` to customize the agent's behavior:
```python
system_prompt = """
Your custom system prompt here.
Define the agent's role, capabilities, and behavior.
"""
```

### Adding New Nodes

Extend the graph by adding new nodes in `graph.py`:
```python
async def my_new_node(state: State):
    # Your node logic here
    return {"messages": [new_message]}

builder.add_node("my_node", my_new_node)
builder.add_edge("chatbot", "my_node")
```

## API Configuration

The agent supports multiple LLM providers:

- **OpenAI**: Set `OPENAI_API_KEY` and `MODEL_NAME`
- **DeepSeek**: Set `DEEPSEEK_API_KEY`, `DEEPSEEK_BASE_URL`, and `DEEPSEEK_MODEL`
- **Other OpenAI-compatible APIs**: Configure base URL and API key accordingly

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please:
1. Check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
2. Open an issue in this repository
3. Join the LangChain community discussions

## Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Package management by [uv](https://docs.astral.sh/uv/)
- Compatible with OpenAI and DeepSeek APIs
