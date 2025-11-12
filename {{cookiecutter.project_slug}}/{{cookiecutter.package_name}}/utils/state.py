from typing import List
from langgraph.types import State

class AgentState(State):
    step: int = 0
    history: List[str] = []
