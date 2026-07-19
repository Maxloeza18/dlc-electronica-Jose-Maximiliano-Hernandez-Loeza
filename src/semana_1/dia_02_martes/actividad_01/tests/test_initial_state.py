from fsm_demo import TrafficLightFSM, TrafficLightState


# Verifica que el estado inicial del semáforo sea RED
def test_initial_state_is_red():
    fsm = TrafficLightFSM()
    assert fsm.state == TrafficLightState.RED