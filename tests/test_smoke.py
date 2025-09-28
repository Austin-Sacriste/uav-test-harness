def test_math_addition():
    """Basic smoke test to confirm pytest working"""
    assert 1 + 1 == 2


def test_environment_imports():
    """Check that core libraries are installed and importable"""
    import pytest
    import serial
    import pymavlink

    assert pytest is not None
    assert serial is not None
    assert pymavlink is not None


def test_hearbeat():
    # check aircraft for heartbeat
    # return heartbeat status and time to collect status
    return


def test_system_components():
    # check aircraft systems
    # all systems go - type of test
    return
