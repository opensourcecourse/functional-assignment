"""
Practice with recursion.
"""
from __future__ import annotations

import random
from typing import Sequence, Type

from pydantic import BaseModel, Field
from faker import Faker

fake_maker = Faker()


class WonderLandCreature(BaseModel):
    name: str = Field(default_factory=fake_maker.name, max_length=15)
    bag: Sequence[WonderLandCreature] | Sequence[Sequence[WonderLandCreature]] = []
    _subclasses = []

    def __init_subclass__(cls, **kwargs):
        cls._subclasses.append(cls)

    @classmethod
    def random_cls(cls) -> Type[WonderLandCreature]:
        return random.choice(cls._subclasses)


class Rabbit(WonderLandCreature):
    pass


class Walrus(WonderLandCreature):
    pass


class PlayingCard(WonderLandCreature):
    pass


class Mushroom(WonderLandCreature):
    pass


class Cheshire(WonderLandCreature):
    pass


def generate_data(recursion_level=0, max_depth=8) -> WonderLandCreature:
    """Generates data """
    bag = [
        generate_data(recursion_level + 1)
        for _ in range(max_depth - random.randrange(recursion_level, max_depth + 1))
    ]
    # maybe nest list more for fun
    if random.randrange(0, 10) > 5:
        bag = [bag]
    cls = WonderLandCreature.random_cls()
    return cls(bag=bag)


def count_creatures(creature: WonderLandCreature) -> int:
    """Count how many creatures are in the recursive structure."""


def classify_creatures(
        creature: WonderLandCreature
) -> dict[str, list[WonderLandCreature]]:
    """
    Separate each of the creatures into a dict of {creature_type_name: [creature]}
    """


def filter_creatures_by_name(creature, character) -> list[WonderLandCreature]:
    """
    Return a list of creatures whose name starts with character.
    """
