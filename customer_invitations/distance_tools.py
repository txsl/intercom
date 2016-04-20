import math

EARTH_RADIUS_KM = 6371


def coords_degs_to_radians(coord_pair_degs):
    """
    Input: Tuple of coordinates (latitude, longitude) pair in degrees
    Output: Tuple of coordinates (latitude, longitude) pair in radians
    """

    # Check input is as we expect before doing anything else
    assert isinstance(coord_pair_degs, dict), \
        "Input is not a dict"

    for attribute in ['latitude', 'longitude']:
        assert attribute in coord_pair_degs, \
            "Input is missing {} value".format(attribute)

    return {
        'latitude': math.radians(coord_pair_degs['latitude']),
        'longitude': math.radians(coord_pair_degs['longitude']),
    }


def calculate_distance(loc1_degs, loc2_degs):
    """
    Returns the distance in km between two pairs of coorindates (latitude and
    longitude).
    Input: loc1_degs, loc2_degs. Both dicts with latitude and longitude keys; values in degrees
    Output: distance in km between the two points
    """

    # No checking of input sanity is done here, since the 'coords_to_radians'
    # function does that (and raises an AssertionError if something is wrong).

    loc1_rads = coords_degs_to_radians(loc1_degs)
    loc2_rads = coords_degs_to_radians(loc2_degs)

    longitude_abs_diff = abs(loc1_rads['longitude'] - loc2_rads['longitude'])

    latitiude_part = math.sin(loc1_rads['latitude']) * math.sin(loc2_rads['latitude'])
    longitude_part = math.cos(loc1_rads['latitude']) * math.cos(loc2_rads['latitude']) * math.cos(longitude_abs_diff)

    # round to 13 dp to avoid floating point precision errors (eg if you pass in the same location)
    central_angle = math.acos(round(latitiude_part + longitude_part, 13))

    return EARTH_RADIUS_KM * central_angle


def filter_by_distance(to_filter, fixed_coord, max_km):
    """
    Take a list of dicts with latitude/longitude coordinates, and returns all
    those within a specific distance
    """

    assert isinstance(to_filter, list)

    filtered = []

    for item in to_filter:
        if calculate_distance(item, fixed_coord) <= max_km:
            filtered.append(item)

    return filtered
