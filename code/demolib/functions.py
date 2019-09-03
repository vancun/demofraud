"""Function library.

To run doctest unit tests, execute as:
    python demolib\functions.py -v
"""

import math

def earth_distance(lat1, lon1, lat2, lon2):
    """Calculate the distance in kilometeres between two locations on Earth.
    
    Examples:
    
    1. Same locations
    >>> earth_distance(39.011566,-119.937831, 39.011566,-119.937831)
    0.0
    
    2. Distance between Colosseum to Eiffel tower (Google: 1435,3 km)
    >>> earth_distance(41.8902, 12.4922, 48.8584, 2.2945)
    1109.2487298102924
    
    """
    r = 6370  # Earth radius in km
    
    lat_dist = math.radians(lat2 - lat1)
    lon_dist = math.radians(lon2 - lon1)
    
    a = math.sin(lat_dist / 2) * math.sin(lat_dist / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(lon_dist / 2) * math.sin(lon_dist / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = r*c
    
    return dist



if __name__ == "__main__":
    import doctest
    doctest.testmod()

