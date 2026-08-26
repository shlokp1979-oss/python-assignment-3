from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def delete_item(request, item_id):

    if request.method == 'DELETE':
        return JsonResponse({
            'success': True,
            'message': 'Item deleted successfully!'
        })

    return JsonResponse({
        'success': False,
        'message': 'Invalid request'
    })