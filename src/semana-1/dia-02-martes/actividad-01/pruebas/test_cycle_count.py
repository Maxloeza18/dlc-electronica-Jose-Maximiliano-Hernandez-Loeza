from fsm_demo import TrafficLightFSM


# Verifica que el contador de ciclos aumente al completar un ciclo
def test_cycle_count_increases_after_full_cycle():
    fsm = TrafficLightFSM()

    # Antes de cualquier transición no debe haber ciclos completos
    assert fsm.cycle_count == 0

    fsm.transition()  # RED -> GREEN
    fsm.transition()  # GREEN -> YELLOW
    fsm.transition()  # YELLOW -> RED

    # Al volver a RED debe haberse completado un ciclo
    assert fsm.cycle_count == 1