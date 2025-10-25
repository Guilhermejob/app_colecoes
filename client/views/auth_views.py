from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse

Client = get_user_model()


@extend_schema(
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "username": {"type": "string", "description": "E-mail ou nickname"},
                "password": {"type": "string"},
            },
        }
    },
    examples=[
        OpenApiExample(
            "Login por email",
            value={"username": "email@exemplo.com", "password": "1234"},
        ),
        OpenApiExample(
            "Login por nickname",
            value={"username": "guilhermejob", "password": "1234"},
        ),
    ],
    responses={
        200: OpenApiResponse(description="Login bem-sucedido"),
        401: OpenApiResponse(description="Credenciais inválidas"),
    },
)
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': "Credenciais Inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "nickname": user.nickname,
            }
        }, status=status.HTTP_200_OK)
        
        

@extend_schema(
    request={
        "application/json": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "password": {"type": "string"},
                "nickname": {"type": "string"},
            },
        }
    },
    responses={201: OpenApiResponse(description="Usuário criado com sucesso")},
)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        nickname = data.get("nickname")
        cpf = data.get("cpf")

        # Validação básica
        if not all([name, email, password, cpf]):
            return Response(
                {"error": "Campos obrigatórios ausentes (name, email, password, cpf)"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Checar duplicatas
        if Client.objects.filter(email=email).exists():
            return Response({"error": "Email já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)

        if nickname and Client.objects.filter(nickname=nickname).exists():
            return Response({"error": "Nickname já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)

        if Client.objects.filter(cpf=cpf).exists():
            return Response({"error": "CPF já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)

        # Criar usuário
        user = Client.objects.create_user(
            email=email,
            name=name,
            nickname=nickname,
            cpf=cpf,
            password=password,
        )

        return Response(
            {
                "message": "Cliente criado com sucesso",
                "data": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "nickname": user.nickname,
                },
            },
            status=status.HTTP_201_CREATED,
        )


@extend_schema(
    request={"application/json": {"type": "object", "properties": {"refresh": {"type": "string"}}}},
    responses={205: OpenApiResponse(description="Logout realizado com sucesso")},
)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            print(token.access_token)
            token.blacklist()
            return Response({"message": "Logout realizado com sucesso"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Token inválido ou já expirado"}, status=status.HTTP_400_BAD_REQUEST)


        
        
        