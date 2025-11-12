from .state import AgentState

def first_node(state: AgentState):
    state.step += 1
    state.history.append("first_node")
    return state

def second_node(state: AgentState):
    state.history.append("second_node")
    return state
