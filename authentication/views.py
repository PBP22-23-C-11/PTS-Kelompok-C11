from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from general.utils import *

@csrf_exempt
def api_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                'status': True,
                'message': 'Successfully Logged In!',
                'data': {
                    'username': user.username,
                    'name': get_user_name(user),
                    'type': get_user_type_string(user),
                },
            }, status=200)
        else:
            return JsonResponse({
                'status': False,
                'message': 'Failed to Login, Account Disabled.',
            }, status=401)

    else:
        return JsonResponse({
            'status': False,
            'message': 'Failed to Login, check your email/password.',
        }, status=401)

@csrf_exempt
def api_logout(request):
    logout(request)
    return JsonResponse({
        'status': True,
        'message': 'Successfully Logged Out!',
    }, status=200)

def api_user_data(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'status': False,
            'message': 'You are not logged in',
        }, status=200)
    else:
        return JsonResponse({
            'status': True,
            'data': {
                'id': request.user.id + 1,
                'username': request.user.username,
                'name': get_user_name(request.user),
                'type': get_user_type_string(request.user),
            },
            'message': 'You are logged in',
        }, status=200)
