"""
This task shows you the easiest way to create immutable data; data-classes.
"""


# Make GeophysicsDepartment a hashable, immutable dataclass
class GeophysicsDepartment:
    """
    A data container.
    """
    student_count: int
    faculty_count: int
    endowment: float = 1_000_000
