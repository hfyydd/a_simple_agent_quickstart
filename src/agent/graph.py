
from langgraph.graph import StateGraph, START, END
from src.agent.state import State
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from src.agent.utils import create_agent
from src.agent.prompts import system_prompt 
from src.agent.tools import get_current_time

load_dotenv()

# 创建ChatOpenAI实例
model_name = os.getenv("DEEPSEEK_MODEL") or os.getenv("MODEL_NAME")
llm = ChatOpenAI(
    model=model_name,
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0
)

async def chatbot_node(state: State):
    """聊天机器人节点"""
    try:
        print("🤖 chatbot节点处理中...")
        print(f"输入消息: {[msg.content for msg in state['messages']]}")

        # 创建agent，添加系统提示
        agent = create_agent("chatbot", llm, [get_current_time], system_prompt)
        
        # create_react_agent需要传入整个状态，而不是消息列表
        response = await agent.ainvoke(state)
        
        print(f"✅ Agent响应类型: {type(response)}")
        
        # create_react_agent返回字典格式 {'messages': [...]}
        # 需要提取新消息（agent的回复），而不是替换整个消息列表
        if isinstance(response, dict) and 'messages' in response:
            # 获取新消息（通常是最后一条，即agent的回复）
            new_messages = response['messages'][len(state['messages']):]
            print(f"✅ 新消息数量: {len(new_messages)}")
            for msg in new_messages:
                print(f"✅ 模型回复: {msg.content[:100]}...")
            
            return {"messages": new_messages}
        else:
            # 如果格式不符合预期，直接返回
            print(f"⚠️ 意外的响应格式: {response}")
            return response
        
    except Exception as e:
        print(f"❌ chatbot节点执行失败: {e}")
        raise e


# 构建LangGraph图
builder = StateGraph(State)

# 添加节点
builder.add_node("chatbot", chatbot_node)

# 添加边
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

# 编译图
graph = builder.compile()




