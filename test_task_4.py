"""Tests for task 4's recursive tasks."""

import pytest

import task_4 as t4


@pytest.fixture(scope="session")
def group():
    """Load family data."""
    return t4.load_data()


@pytest.fixture(scope="session")
def obama(group):
    """Return Barack Obama from Group. Thanks Obama..."""
    return group["@I2194@"]


@pytest.fixture(scope="session")
def lincoln(group):
    """Get ol' Honest Abe."""
    return group["@I317@"]


class TestCountPeople:
    """Tests for counting people."""

    def test_count_obama_ancestors(self, group, obama):
        """Ensure we can count a person's known ancestors with default params."""
        out = t4.count_people(obama, group)
        # In this test data, there are 5 known ancestors of Barack Obama.
        assert out == 5

    def test_count_childless_parents(self, group, lincoln):
        """Check that a persons parents all have children (predicate check)."""
        out = t4.count_people(
            lincoln,
            group,
            direction="parents",
            predicate=lambda x: len(x.children) == 0,
        )
        assert out == 0

    def test_lincoln_old_ancestors(self, group, lincoln):
        """Check the number of old ancestors Lincoln had."""

        def is_old(person):
            try:
                return person.age > 70
            except ValueError:
                return False

        out = t4.count_people(
            lincoln,
            group,
            direction="parents",
            predicate=is_old,
        )
        # There are 18 people older than 70 in Lincoln's tree.
        assert out == 18
