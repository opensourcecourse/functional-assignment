"""Task to create immutable data with data-classes."""


# Make GeophysicsDepartment a hashable, immutable dataclass
class GeophysicsDepartment:
    """A class to represent the geophysics department."""

    student_count: int
    faculty_count: int
    endowment: float = 1_000_000
