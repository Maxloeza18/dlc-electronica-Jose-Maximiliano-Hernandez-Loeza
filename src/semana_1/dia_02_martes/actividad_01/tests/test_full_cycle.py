from fsm_demo import TrafficLightFSM, TrafficLightState


# Verifica que después de tres transiciones el semáforo vuelva a RED
def test_full_cycle_returns_to_red():
    fsm = TrafficLightFSM()

    fsm.transition()  # RED -> GREEN
    fsm.transition()  # GREEN -> YELLOW
    fsm.transition()  # YELLOW -> RED

    assert fsm.state == TrafficLightState.RED