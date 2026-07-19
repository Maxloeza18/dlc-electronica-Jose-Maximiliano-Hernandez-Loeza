from door_fsm import DoorFSM, DoorState


def test_open_from_closed():
    fsm = DoorFSM()
    fsm.open()
    assert fsm.state == DoorState.OPEN