from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token

# 1. Login view
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        context = {
            'status': HTTP_200_OK,
            "message": 'User has been logged in successfully',
            "token": token.key,
        }
        return Response(context, status=HTTP_200_OK)
    else:
        context = {
            'status': HTTP_404_NOT_FOUND,
            "message": "Invalid credentials",
        }
        return Response(context, status=HTTP_404_NOT_FOUND)

# 2. Register view
@api_view(["POST"])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    
    if User.objects.filter(username=username).exists():
        context = {
            'status': HTTP_400_BAD_REQUEST,
            "message": "Username already exists",
        }
        return Response(context, status=HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    
    context = {
        'status': HTTP_200_OK,
        "message": "User has been registered successfully",
    }
    return Response(context, status=HTTP_200_OK)

# 3. Logout view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    auth_logout(request)
    context = {
        'status': HTTP_200_OK,
        "message": "User has been logged out successfully",
    }
    return Response(context, status=HTTP_200_OK)
