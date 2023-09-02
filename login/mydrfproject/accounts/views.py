from django.shortcuts import render

# Create your views here.
# accounts/views.py
from rest_framework import generics, permissions
from knox.models import AuthToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Register USER API
class register_user(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({"user": serializer.data,
                         "token": AuthToken.objects.create(user)[1]
                         })


# accounts/views.py

# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.exceptions import ObjectDoesNotExist

# from .models import CustomUser

# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = None
#         if '@' in username:
#             try:
#                 user = CustomUser.objects.get(email=username)
#             except ObjectDoesNotExist:
#                 pass

#         if not user:
#             user = authenticate(username=username, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)

#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# LOGIN
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as knoxLoginView

class user_login(knoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format = None):
        serializer = AuthTokenSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(user_login,self).post(request, format=None)



# accounts/views.py

# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     # print("token to delete")

#     if request.method == 'POST':
#         try:
#             # Delete the user's token to logout
#             # print("token to delete in if")

#             request.user.auth_token.delete()
#             # print("token deleted")
#             return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# LOGOUT
# from django.contrib.auth import logout
# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from knox.views import LogoutView as knoxLogoutView

# class LogoutView(knoxLogoutView):
#     permission_classes = (permissions.IsAuthenticated,)

#     def post(self, request, format=None):
#         logout(request)  # Use Django's logout function
#         return Response({'message': 'Successfully logged out.'})



# from knox.views import LogoutView as knoxLogoutView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes

# class LogoutView(knoxLogoutView):
#     permission_classes = (IsAuthenticated,)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def custom_user_logout(request):
#     LogoutView.as_view()(request._request)
#     return Response({'message': 'Successfully logged out.'})
