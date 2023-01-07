"""Task 4: Practice with recursion."""
from pathlib import Path
from typing import Callable, Dict, Optional, Set

import pydantic
from typing_extensions import Literal

# --- models for family data


class Individual(pydantic.BaseModel):
    """An individual model.

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

    @classmethod
    def from_element(cls, el):
        """Populate Family from element."""
        data = dict(
            id=el.get_pointer(),
            name=" ".join(el.get_name()),
            surname=el.get_name()[-1],
            gender=el.get_gender(),
            birth_year=el.get_birth_year(),
            death_year=el.get_death_year(),
        )
        return cls(**data)


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
    person: Individual,
    direction: Literal["children", "parents"] = "children",
    predicate: Callable[[Individual], bool] = lambda x: True,
):
    """
    Count people in an individuals family tree which meet some requirement.

    Parameters
    ----------
    person
        The person with which to start.
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
    >>> random_person = data[random.choice(list(data))]
    >>> count_people(random_person, predicate=lambda x: len(x.children) > 2)
    """


if __name__ == "__main__":
    data = load_data()
