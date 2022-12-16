from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.sites import requests
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import SignupSerializer, LoginSerializer

KAKAO_REST_API_KEY = "3ec9ad497bc0ec9335ae6a557b415c0a"
KAKAO_REDIRECT_URI = "http://127.0.0.1:3000/oauth/callback/kakao/"
KAKAO_AUTH_URI = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
    if serializer.validated_data['email'] == "None":
        return Response({"message" : "올바르지 않은 회원 정보입니다."}, status=status.HTTP_400_BAD_REQUEST)

    response = {
        'refresh_token' : serializer.validated_data['refresh_token'],
        'access_token' : serializer.validated_data['access_token']
    }
    return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def logout(request):
    refresh_token = request.data["refresh_token"]
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response("Successful Logout", status=status.HTTP_200_OK)

def kakao_login(request):
    client_id = KAKAO_REST_API_KEY
    code = request.GET.get("code", None)
    redirect_uri = KAKAO_REDIRECT_URI
    auth_uri = KAKAO_AUTH_URI
    token_request = requests.get(
        f"{auth_uri}client_id={client_id}&redirect_uri={redirect_uri}&code={code}")
    token_json = token_request.json()

    kakao_access_token = token_json.get("access_token")

    profile_request = requests.post(
        "https://kapi.kakao.com/v2/user/me",
        headers={"Authorization": f"Bearer {kakao_access_token}"},
    )
    profile_json = profile_request.json()
    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email", None)

    if email is None:
        return Response({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    nickname = kakao_account.get("profile").get("nickname")

    try:
        user = get_user_model().objects.get(email=email)
        if user.is_kakao:
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            update_last_login(None, user)
            results = {
                'email': email,
                'nickname': user.nickname,
                'refresh_token': refresh_token,
                'access_token': access_token,
            }
            return Response(results, status = status.HTTP_200_OK)
    except get_user_model().DoesNotExist:
        user = get_user_model().objects.create(
            email=email,
            nickname=nickname,
            is_kakao=True,
            phone="",
        )
        user.set_unusable_password()
        user.save()

        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        update_last_login(None, user)

        results = {
            'email': email,
            'nickname': user.nickname,
            'refresh_token': refresh_token,
            'access_token': access_token,
        }
        return Response(results, status=status.HTTP_201_CREATED)
    else:
        return Response({'message':'user already exist'}, status=status.HTTP_400_BAD_REQUEST)
