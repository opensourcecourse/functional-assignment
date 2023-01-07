"""Tests for task3."""
from dataclasses import FrozenInstanceError, is_dataclass

import pytest

from task_3 import GeophysicsDepartment


def test_is_dataclass():
    """GP should be a dataclass."""
    gp = GeophysicsDepartment(student_count=30, faculty_count=8)
    assert is_dataclass(gp)


def test_immutable():
    """Ensure GeophysicsDepartment is immutable."""
    gp = GeophysicsDepartment(student_count=10, faculty_count=3)
    with pytest.raises(FrozenInstanceError):
        gp.student_count = 12_000
