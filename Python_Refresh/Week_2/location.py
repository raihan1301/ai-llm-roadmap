import sys

def main():
    coordinates = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"latitude: {coordinates[0]}")

    latitude, longitude = coordinates
    print(f"longitude: {longitude}")

    print(f"{sys.getsizeof(coordinates)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

main()