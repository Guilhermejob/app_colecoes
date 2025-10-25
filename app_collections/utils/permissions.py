from rest_framework.response import Response
from rest_framework import status


def check_collection_ownership(collection, user):
    """
    Verifica se o usuário autenticado é o proprietário da coleção.
    Retorna uma resposta de erro se não for, caso contrário None.
    """
    if collection.owner != user.id:
        return Response(
            {"error": "Vocé nao tem permissão para modificar essa coleçao"},
            status=status.HTTP_403_FORBIDDEN
        )
    return None
    
def check_collection_access_permission(collection, user):
    """
    Verifica se o usuário pode visualizar a coleção.
    - Se a coleção for pública, qualquer um pode ver.
    - Se for privada, apenas o dono pode acessar.
    Retorna Response de erro caso o usuário não tenha permissão, ou None se tudo ok.
    """
    
    # Coleções públicas podem ser vistas por qualquer um
    if collection.is_public:
        return None 
    
    # Apenas o dono pode ver coleções privadas
    if user.is_authenticated and collection.owner == user:
        return None 
    
    # Caso contrário, acesso negado
    return Response(
    {"error": "Você não tem permissão para visualizar essa coleção."},
    status=status.HTTP_403_FORBIDDEN
)

        
    