import types
from itertools import chain


UNEXPECTED_TYPE_ERR_MSG = "Unexpected object type in list. Got {}, expected int or list."
LIST_NOT_PASSED = "Object passed to function is {}, not a list"


def flatten_list(nested_list):
    """
    Expects a list of ints and lists to be passed in.
    Any nested list will be flattened.
    Returns a flattened list.
    """

    # print(isinstance(nested_list, list), nested_list)
    # Guard for things passed in which are not lists
    assert isinstance(nested_list, list),\
        LIST_NOT_PASSED.format(type(nested_list))

    # using chain since this should provide better performance than iterating
    # through the list directly

    # We don't use chain.from_iterable, since not every item in the list is
    # iterable (ie an int, is not iterable)
    chained = chain(nested_list)

    # initialise output list, which will be flattened
    flattened = []

    for elem in chained:

        # This is needed since a Bool is a subset of an int, so not caught
        # below like other objects are.
        assert not type(elem) == bool,\
            UNEXPECTED_TYPE_ERR_MSG.format(type(elem))

        if isinstance(elem, int):
            # if int, append to the flattened list
            flattened.append(elem)
        elif isinstance(elem, list):
            # if it's another list, use recursion to get the flattened list
            # and add it to the flattened list in this function call
            flattened += flatten_list(elem)
        else:
            # raise exception if object not a list or int
            raise Exception(UNEXPECTED_TYPE_ERR_MSG.format(type(elem)))

    return flattened


if __name__ == '__main__':
    print('Flatten list function. Sample input/output')
    for item in [
                [],
                [1, 2, 3, 4, 5],
                [1, 2, [3, 4], [[2, 3, [1, 1], [5, 8, [7, 6]]], 2]]
                ]:
        print('Input:', item, 'Output:', flatten_list(item))
