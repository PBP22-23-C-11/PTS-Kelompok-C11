import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

# @csrf_exempt
# def api_register_one(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.isi_valid():
#             form.save()
#             return JsonResponse({'success': True}, status=201)
#         return JsonResponse({'success': False}, status=400)
#     return HttpResponse(status=404)

@csrf_exempt
def api_register_one(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if username != None and password1 != None and password2 != None:
            if password1 != password2:
                return JsonResponse({'success': False, 'message': 'Re-typed password is not the same'}, status=400)
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
            except:
                return JsonResponse({'success': False, 'message': 'User already exists'}, status=400)
            return JsonResponse({'success': True}, status=400)
        return JsonResponse({'success': False, 'message': 'Bad Request'}, status=400)
    return HttpResponse(status=404)

@csrf_exempt
@login_required
def api_register_two(request):
    if request.method == 'POST':
        user_type = request.POST.get('type')
        if 'type' != None:
            if user_type == 'umkm' and 'name' in request.POST:
                name = request.POST.get('name')
                UMKM.objects.create(user=request.user, name=name)
                return JsonResponse({'success': True}, status=201)
            elif user_type == 'customer' and 'first_name' in request.POST and 'last_name' in request.POST:
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                Customer.objects.create(user=request.user, first_name=first_name, last_name=last_name)
                return JsonResponse({'success': True}, status=201)
        return JsonResponse({'success': False}, status=400)
    return HttpResponse(status=404)