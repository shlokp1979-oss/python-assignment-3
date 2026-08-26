from django.shortcuts import render
from .utils import calculate_distance


# Task 4
def search_by_distance(request):

    pickup_points = [
        {
            'name': 'Pickup Point 1',
            'address': 'Navrangpura, Ahmedabad',
            'lat': 23.0365,
            'lng': 72.5660
        },
        {
            'name': 'Pickup Point 2',
            'address': 'Satellite, Ahmedabad',
            'lat': 23.0300,
            'lng': 72.5100
        },
        {
            'name': 'Pickup Point 3',
            'address': 'Vastrapur, Ahmedabad',
            'lat': 23.0400,
            'lng': 72.5300
        },
        {
            'name': 'Pickup Point 4',
            'address': 'Maninagar, Ahmedabad',
            'lat': 22.9950,
            'lng': 72.6020
        },
        {
            'name': 'Pickup Point 5',
            'address': 'Bopal, Ahmedabad',
            'lat': 23.0300,
            'lng': 72.4650
        }
    ]

    results = []

    if request.method == 'POST':

        try:
            user_lat = float(request.POST.get('latitude'))
            user_lng = float(request.POST.get('longitude'))

        except (ValueError, TypeError):

            return render(
                request,
                'search.html',
                {
                    'error': 'Please enter valid latitude and longitude.'
                }
            )

        for point in pickup_points:

            distance = calculate_distance(
                user_lat,
                user_lng,
                point['lat'],
                point['lng']
            )

            point['distance'] = round(distance, 2)

            results.append(point)

        results.sort(
            key=lambda x: x['distance']
        )

    return render(
        request,
        'search.html',
        {
            'results': results
        }
    )


# Task 2
def show_restaurant_location(request):

    address = request.GET.get(
        'address',
        'IIM Ahmedabad, Gujarat'
    )

    return render(
        request,
        'restaurant_location.html',
        {
            'address': address
        }
    )