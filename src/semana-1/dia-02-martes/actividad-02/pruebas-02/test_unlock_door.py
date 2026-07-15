from door_fsm import DoorFSM, DoorState


def test_unlock_from_locked():
    fsm = DoorFSM()
    fsm.lock()
    fsm.unlock()
    assert fsm.state == DoorState.CLOSED