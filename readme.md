Note: A working Python 3.5 installation is needed. All modules imported are part of the standard Python install; no other external packages are used.

# Flatten List

All commands must be run within the `flatten_list` directory of this repository.

The function is located in `flatten_list.py`. To run the function and see some sample input/output, call `python flatten_list.py`.

Tests are located in `test_flatten_list.py` and can be run by calling `python test_flatten_list.py`.


# Customer Invitations

`processing_tools.py` deals with handling files, parsing their contents and printing the results/saving it to a file. Its tests can be run by calling `python test_processing_tools.py`.

`distance_tools.py` contains a function which calculate the distance between two co-ordinates, as well as some helper functions for this. Tests can be run by calling `python test_distance_tools.py`.

`main.py` links the various helper functions together in the function `main()` and is called when running `python main.py`. This will parse the data in `customers.json`, and print the filtered list to the terminal, as well as save it to a file called `sorted_filtered_customers.json`.
