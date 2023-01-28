"""Fun with higher order functions."""
REGISTERED_FUNCTIONS = {}


def register(name):
    """
    Register a function using a given name.

    Examples
    --------
    >>> @register('first')
    ... def first_function():
    ...    pass

    >>> assert 'first' in REGISTERED_FUNCTIONS
    >>> assert REGISTERED_FUNCTIONS['first'] == first_function
    """
    # fill in your implementation here.
