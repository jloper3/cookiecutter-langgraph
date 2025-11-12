from {{ cookiecutter.package_name }}.agent import graph
from {{ cookiecutter.package_name }}.utils.state import AgentState

def test_graph_runs():
    initial = AgentState()
    result = graph.invoke(initial, {"model_name": "openai"})
    assert isinstance(result, AgentState)
    assert "first_node" in result.history
