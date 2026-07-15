from door_fsm import DoorFSM, DoorState


def test_initial_state_is_closed():
    fsm = DoorFSM()
    assert fsm.state == DoorState.CLOSED