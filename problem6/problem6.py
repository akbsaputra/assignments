import functools


def process_record(record, transforms):
    """
    Given an item and a dictionary mapping keys to functions,
    use the given functions to transform the item's values.

    NOTE: This code currently has a bug in it!

    Arguments:
        * record : dict[str, Any] - A dictionary with data to be modified.
                                    Every key in the dictionary is a string.
        * transforms : dict[str, Callable] - A dictionary mapping keys to functions.
                                             Every key in transforms is a key from record.
    """
    # This code maps each item in the dictionary to a tuple (key, new_value)
    #   item[0] is the key, item[1] is the value
    # calling dict() on an iterable of tuples creates a dictionary
    return dict(
        map(lambda item: (item[0], transforms[item[0]](item[1])), record.items())
    )
