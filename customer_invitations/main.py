from distance_tools import filter_by_distance
from processing_tools import ingest_file, sort_users_by_id, print_customers, save_customers_to_file

OFFICE_COORDS = {
    'latitude': 53.3381985,
    'longitude': -6.2592576,
}
MAX_DISTANCE = 100


def main():
    all_customers = ingest_file('customers.json')

    filtered_customers = filter_by_distance(
        all_customers,
        OFFICE_COORDS,
        MAX_DISTANCE
    )

    sorted_customers = sort_users_by_id(filtered_customers)

    print_customers(sorted_customers)

    save_customers_to_file(sorted_customers, 'sorted_filtered_customers.json')

if __name__ == '__main__':
    main()
