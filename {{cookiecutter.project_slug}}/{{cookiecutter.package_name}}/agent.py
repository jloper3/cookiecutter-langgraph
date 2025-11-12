from typing import TypedDict, Literal
from langgraph.graph import StateGraph, START, END
from .utils.nodes import first_node, second_node
from .utils.state import AgentState

class GraphContext(TypedDict):
    model_name: Literal["openai", "anthropic"] = "openai"

workflow = StateGraph(AgentState, context_schema=GraphContext)
workflow.add_node("first_node", first_node)
workflow.add_node("second_node", second_node)
workflow.add_edge(START, "first_node")
workflow.add_edge("first_node", "second_node")
workflow.add_edge("second_node", END)

graph = workflow.compile()
