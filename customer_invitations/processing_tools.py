import warnings
import json


DATA_FIELDS = ['user_id', 'name', 'latitude', 'longitude']


def parse_customer_json(cust_json):
    # Remove whitespace, newline characters etc
    cust_json = cust_json.rstrip()

    # turn JSON into dict
    cust_parsed = json.loads(cust_json)

    for field in DATA_FIELDS:
        assert field in cust_parsed, \
            "field '{}' missing in line: {}".format(field, cust_json)

    assert isinstance(cust_parsed['user_id'], int), \
        "user_id not an int in line: {}".format(cust_json)

    for coord in ['latitude', 'longitude']:
        try:
            cust_parsed[coord] = float(cust_parsed[coord])
        except ValueError as ex:
            raise Exception("Could not cast {} to float (value: '{}')".format(
                coord,
                cust_parsed[coord]
            )) from ex

    return cust_parsed


def ingest_file(filename):
    with open(filename, 'r') as opened:

        customers = []

        for line in opened:
            try:
                customers.append(parse_customer_json(line))
            except Exception as ex:
                warnings.warn("Skipping line due to error: '{}'".format(
                    line.rstrip(),
                    ex,
                ))

    return customers


def sort_users_by_id(unsorted_customers):
    return sorted(unsorted_customers, key=lambda k: k['user_id'])


def print_customers(customers):
    print("User ID, Name")
    for cust in customers:
        print("{}, {}".format(cust['user_id'], cust['name']))


def save_customers_to_file(customers, filename='updated_customers.json'):
    with open(filename, 'w+') as fileh:
        for cust in customers:
            fileh.write(json.dumps(cust) + '\n')

    print("Customers saved to {}".format(filename))
