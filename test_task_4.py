"""
Tests for task 4's recursive tasks.
"""

import pytest

import task_4 as t4


def create_recursive(count, max_count, creature, width=1):
    """Recursively create creatures."""
    if count < max_count:
        bag = [
            create_recursive(count + 1, max_count, creature)
            for _ in range(width)
        ]
    else:
        bag = []
    return creature(bag=bag)


@pytest.fixture()
def shallow_creature():
    """A simple shallow creature."""
    return t4.Cheshire(bag=[])


@pytest.fixture()
def creature_one_deep():
    """One deep creature."""
    bag = [t4.PlayingCard(), t4.Mushroom(), t4.Cheshire(), t4.Walrus()]
    return t4.Rabbit(bag=bag)


@pytest.fixture()
def mushroom_10():
    """Create 10 deep mushrooms."""
    return create_recursive(0, 10, t4.Mushroom)


class TestCount:
    """Test counting creatures."""

    def test_shallow(self, shallow_creature):
        assert t4.count_creatures(shallow_creature) == 1

    def test_test_one_deep(self, creature_one_deep):
        assert t4.count_creatures(creature_one_deep) == 5

    def test_10_deep(self, mushroom_10):
        assert t4.count_creatures(mushroom_10) == 10


class TestClassifyCreatures:
    """Tests for separating creatures."""
