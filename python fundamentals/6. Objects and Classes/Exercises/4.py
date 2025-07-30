class Town():
    latitude = "0°N"
    longitude = "0°E"
    def __init__(self, name: str):
        self.name = name

    def set_latitude(self, latitude):
        Town.latitude = latitude

    def set_longitude(self, longitude):
        Town.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {Town.latitude} | Longitude: {Town.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
