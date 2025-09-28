def test_math_addition():
    """Basic smoke test to confirm pytest working"""
    assert 1+1 == 2

def test_environment_imports():
    """Check that core libraries are installed and importable"""
    import pytest
    import serial
    import pymavlink

    assert pytest is not None
    assert serial is not None
    assert pymavlink is not None