from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


from .serializers import SignupSerializer, LoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"message": "Request Body Error."}, status=409)
    if serializer.validated_data['email'] == "None":
        return Response({"message" : "올바르지 않은 회원 정보입니다."}, status=400)

    response = {
        'refresh_token' : serializer.validated_data['refresh_token'],
        'access_token' : serializer.validated_data['access_token']
    }
    return Response(response, status=200)



@api_view(['POST'])
def logout(request):
    refresh_token = request.data["refresh_token"]
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response("Successful Logout", status=200)