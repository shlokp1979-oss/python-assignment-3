import requests


API_KEY = "YOUR_GOOGLE_API_KEY"


def get_location(address):

    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": address,
        "key": API_KEY
    }

    response = requests.get(url, params=params)

    data = response.json()

    if data["status"] == "OK":

        location = data["results"][0]["geometry"]["location"]

        return location["lat"], location["lng"]

    return None, None


address = "IIM Ahmedabad, Gujarat"

lat, lng = get_location(address)

print("Address:", address)
print("Latitude:", lat)
print("Longitude:", lng)