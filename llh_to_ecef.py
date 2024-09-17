# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat long HAE
# Converts LLH components to ECEF

# Parameters:
# lat: LLH latitude in deg
# long: LLH longitude in deg
# HAE: LLH HAE in km
# Output:
# Prints r_x (km), r_y (km), and r_z (km)
#
# Written by Samuel Jacobson
# Other contributors: None
#

# import Python modules
import math
import sys

# Constants
R_E_KM = 6378.137  # Earth's equatorial radius in kilometers
E_E = 0.08181919221456  # Earth's eccentricity

# Helper function to calculate the denominator for the prime vertical radius of curvature
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0 - (ecc ** 2) * (math.sin(lat_rad) ** 2))

# Initialize script arguments
lat_deg = float('nan')  # Latitude in degrees
long_deg = float('nan')  # Longitude in degrees
HAE = float('nan')  # Height Above Ellipsoid in kilometers

# Parse script arguments
if len(sys.argv) == 4:
    lat_deg = float(sys.argv[1])
    long_deg = float(sys.argv[2])
    HAE = float(sys.argv[3])
else:
    print('Usage: python3 llh_to_ecef.py lat long HAE')
    sys.exit()

# Convert latitude and longitude to radians
lat_rad = math.radians(lat_deg)
lon_rad = math.radians(long_deg)

# Calculate the prime vertical radius of curvature
denom = calc_denom(E_E, lat_rad)
c_E = R_E_KM / denom

# Calculate the ECEF coordinates
r_x_km = (c_E + HAE) * math.cos(lat_rad) * math.cos(lon_rad)
r_y_km = (c_E + HAE) * math.cos(lat_rad) * math.sin(lon_rad)
r_z_km = (c_E * (1 - E_E ** 2) + HAE) * math.sin(lat_rad)

# Print the ECEF coordinates
print(r_x_km)
print(r_y_km)
print(r_z_km)
