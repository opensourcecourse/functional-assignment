"""Task 4: Practice with recursion."""
import datetime
from pathlib import Path
from typing import Callable, Dict, Optional, Set

import pydantic
from typing_extensions import Literal

# --- models for family data


class Individual(pydantic.BaseModel, frozen=True):
    """
    A model of an individual.

    Parents, children, and spouses are keys to other
    individual ids.
    """

    id: str
    name: str
    surname: str
    gender: Literal["M", "F"]
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    parents: Set[str] = set()
    children: Set[str] = set()
    spouses: Set[str] = set()

    @property
    def age(self) -> Optional[int]:
        """Return the estimated age of the person."""
        birth_year = self.birth_year
        if birth_year is None or birth_year < 0:
            raise ValueError(f"Unknown Age of {self.name}: {self.id}")
        end_year = self.death_year
        if end_year is None or end_year < 0:
            end_year = datetime.datetime.now().year
        return end_year - birth_year


class Group(pydantic.BaseModel):
    """A dict-like container for individuals."""

    individuals: Dict[str, Individual] = {}

    def __getitem__(self, item):
        return self.individuals[item]


def load_data(path=None):
    """Loads the family tree data into memory."""
    if path is None:
        path = Path(__file__).absolute().parent / "data" / "family_tree.json"
    return Group.parse_file(path)


def count_people(
    individual: Individual,
    group: Group,
    direction: Literal["children", "parents"] = "parents",
    predicate: Callable[[Individual], bool] = lambda x: True,
) -> int:
    """
    Count people in an individuals family tree which meet some requirement.

    Parameters
    ----------
    individual
        The person with which to start.
    group
        The group to which the person belongs.
    direction
        The direction to travel (down through children or up through parents).
    predicate
        A callable which take an individual as the only argument and returns
        True or False if they meet the requirement.

    Examples
    --------
    >>> import random
    >>> data = load_data()
    >>> # Count direct descendants with more than two children.
    >>> person = data[random.choice(list(data))]
    >>> count = count_people(person, predicate=lambda x: len(x.children) > 2)

    Notes
    -----
    This function will also count the initial individual if they pass the
    predicate.
    """
