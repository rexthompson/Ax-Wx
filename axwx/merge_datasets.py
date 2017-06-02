"""
Functions to combine Washington State Patrol and Weather Underground datasets into single enhanced DF
"""

from geopy.distance import vincenty  # note: had to pip install geopy


def get_bounding_box(coords, dist_mi):
    """
    Calculate lat/lon bounding box for distance from reference location
    :param coords: 2-tuple
        (latitude, longitude) pair for reference location 
    :param dist_mi: numeric
        length of shortest distance of bounding box, in miles
    :return: lists of bounding box coordinate limits for latitude and longitude
    """
    lon_dist_mi = dist_mi * 1 / vincenty(coords, (coords[0], coords[1] + 1)).miles
    lat_dist_mi = dist_mi * 1 / vincenty(coords, (coords[0] + 1, coords[1])).miles

    lat_bounds_deg = [coords[0] - lat_dist_mi, coords[0] + lat_dist_mi]
    lon_bounds_deg = [coords[1] - lon_dist_mi, coords[1] + lon_dist_mi]

    return lat_bounds_deg, lon_bounds_deg


