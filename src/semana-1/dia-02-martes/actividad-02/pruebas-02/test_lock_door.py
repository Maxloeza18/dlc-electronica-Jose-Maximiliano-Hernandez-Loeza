from door_fsm import DoorFSM, DoorState


def test_lock_from_closed():
    fsm = DoorFSM()
    fsm.lock()
    assert fsm.state == DoorState.LOCKED