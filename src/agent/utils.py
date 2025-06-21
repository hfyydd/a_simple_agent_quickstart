from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI



# Create agents using configured LLM types
def create_agent(agent_name: str, llm: ChatOpenAI, tools: list, prompt_template: str):
    """Factory function to create agents with consistent configuration."""
    return create_react_agent(
        name=agent_name,
        model=llm,
        tools=tools,
        prompt=prompt_template,
    )