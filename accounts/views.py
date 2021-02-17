from django.contrib import auth
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from .UserSerializer import UserSerializer
from .forms import UserLoginForm, UserRegistrationForm, MyUserRegistrationForm

@api_view(["GET"])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_user(request):
    payload = json.loads(request.body)
    try:

        user = User.objects.create(
            id=payload["id"],
            username=payload["username"],
            password=payload["password"],
            email=payload["email"]
        )
        user.save()
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
def update_user(request, user_id):
    payload = json.loads(request.body)
    try:
        user = User.objects.get(id=user_id)
        user.set_password(payload['password'])
        user.save()
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def gethome(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username_or_email']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'forms': login_form})


def register(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        myuser_form = MyUserRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and myuser_form.is_valid():
            user = user_form.save()
            myuser = myuser_form.save(commit=False)
            myuser.user = user
            myuser.save()

            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form = UserRegistrationForm()
        myuser_form = MyUserRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': myuser_form})


def logout(request):
    auth.logout(request)
    return redirect('/')
