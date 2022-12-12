from django.contrib.auth.models import User
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
                    'id': user.id,
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

def api_user_data(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'name': get_user_name(user),
        'type': get_user_type_string(user),
    }, status=200)
