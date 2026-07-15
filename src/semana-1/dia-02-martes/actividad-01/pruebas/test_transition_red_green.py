from fsm_demo import TrafficLightFSM, TrafficLightState


# Verifica que la primera transición cambie de RED a GREEN
def test_transition_from_red_to_green():
    fsm = TrafficLightFSM()
    fsm.transition()
    assert fsm.state == TrafficLightState.GREEN