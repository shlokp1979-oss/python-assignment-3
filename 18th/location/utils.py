import math


def calculate_distance(lat1, lng1, lat2, lng2):

    R = 6371

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)

    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlng / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return R * c


def find_nearby_cafes(user_lat, user_lng, cafes):

    nearby = []

    for cafe in cafes:

        distance = calculate_distance(
            user_lat,
            user_lng,
            cafe['lat'],
            cafe['lng']
        )

        if distance <= 3:
            cafe['distance'] = round(distance, 2)
            nearby.append(cafe)

    return nearby