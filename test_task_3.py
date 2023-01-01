"""
Tests for task3.
"""
import pytest

from task_3 import GeophysicsDepartment

from dataclasses import FrozenInstanceError, is_dataclass


def test_is_dataclass():
    """GP should be a dataclass."""
    gp = GeophysicsDepartment()
    assert is_dataclass(gp)


def test_immutable():
    """Ensure GeophysicsDepartment is immutable."""
    gp = GeophysicsDepartment(student_count=10, faculty_count=3)
    with pytest.raises(FrozenInstanceError):
        gp.student_count = 12_000
