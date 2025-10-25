from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view

from app_collections.models.diecast_collection import DiecastCollection
from app_collections.models.diecast_collection_item import DiecastCollectionItem
from app_collections.serializers.collection_serializer import (
    CollectionSerializer, 
    CollectionItemSerializer
)
from app_collections.utils.permissions import check_collection_access_permission, check_collection_ownership



@extend_schema_view(
    get=extend_schema(responses=CollectionItemSerializer,description="Lista todos os itens de uma coleção ou um item específico."),
    post=extend_schema(request=CollectionItemSerializer,responses={201: CollectionItemSerializer},description="Adiciona um novo item à coleção especificada."),
    patch=extend_schema(request=CollectionItemSerializer,responses={200: CollectionItemSerializer},description="Atualiza parcialmente um item da coleção."),
    delete=extend_schema(responses={204: None},description="Remove um item de uma coleção específica."),
)

class DiecastCollectionItemApiView(APIView):
    """
    Endpoint para gerenciar itens de uma coleçao (GET, POST, PATCH, DELETE)
    """
    
    
    def _get_collection_with_permission(self, collection_id, user, require_owner=False):
        """Busca a coleção e valida o acesso (respeita is_public e owner)."""
        collection = get_object_or_404(DiecastCollection, pk=collection_id)
        if require_owner:
            perm = check_collection_ownership(collection, user)
            if perm:
                return None, perm
        else:
            perm = check_collection_access_permission(collection, user)
            if perm:
                return None, perm
        return collection, None
    
    
    def get(self, request, collection_id, id=None):
        """
        Retorna todos os itens de uma coleçao ou um item específico dentro dela
        """
        
        collection, perm = self._get_collection_with_permission(collection_id, request.user)
        
        if perm:
            return perm
    
        if id:
            item = get_object_or_404(DiecastCollectionItem, pk=id, collection=collection)
            serializer = CollectionItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)

        items = DiecastCollectionItem.objects.filter(collection=collection)
        serializer = CollectionItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, collection_id):
        """
        Adiciona um novo item à coleçao especificada
        """
        collection, perm = self._get_collection_with_permission(collection_id, request.user, require_owner=True)
        if perm:
            return perm
        
        serializer = CollectionItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(collection=collection)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

    def patch(self, request, collection_id, id):
        """Atualiza parcialmente um item da coleção."""
        collection, perm = self._get_collection_with_permission(collection_id, request.user, require_owner=True)
        
        if perm:
            return perm

        item = get_object_or_404(DiecastCollectionItem, pk=id, collection=collection)
        serializer = CollectionItemSerializer(item, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, collection_id, id):
        """Remove um item da coleção."""
        
        collection, perm = self._get_collection_with_permission(collection_id, request.user, require_owner=True)
        
        if perm:
            return perm

        item = get_object_or_404(DiecastCollectionItem, pk=id, collection=collection)
        item.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

        

class DiecastCollectionApiView(APIView):
    """
    Endpoint que gerencia as coleções de minaturas do cliente (GET, POST, PATCH, DELETE)
    """

    def get(self, request, id=None):
        """
        Get /Collections/     -> lista colecões
        Get /Collections/{id} -> detalhe de uma coleção (respeita is_public / owner)  
        """
        

        
        # Se veio um id, mostra uma coleção específica
        if id:
            try:
                collection = DiecastCollection.objects.get(pk=id)
                
            except DiecastCollection.DoesNotExist:
                return Response({"error": "Coleçao nao encontrada"}, status=status.HTTP_404_NOT_FOUND)
            
            permission_error = check_collection_access_permission(collection, request.user)
            
            if permission_error:
                return permission_error
            
            serializer = CollectionSerializer(collection)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if request.user.is_authenticated:
            collections = DiecastCollection.objects.filter(
                Q(is_public=True) | Q(owner=request.user)
            ).distinct()
        else:
            collections = DiecastCollection.objects.filter(is_public=True)
            
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def post(self, request):
        """
        Cria uma nova coleçao
        """
        
        serializer = CollectionSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(
                {"Message":"Coleçao criada com sucesso", "data":serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error":"Erro ao criar coleçao", "details":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST    
        )
        
    def patch(self, request, id):
        """
        Atualiza os dados da coleçao
        """
        
        try:
            collection = DiecastCollection.objects.get(pk = id)
        except DiecastCollection.DoesNotExist:
            return Response({"Error":"A coleçao nao foi encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        permission_error = check_collection_ownership(collection, request.user)
        if permission_error:
            return permission_error
        
        serializer = CollectionSerializer(collection, data = request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"Coleçao atualizada com sucesso", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        
        return Response(
            {"error":"Erro ao atualizar a coleçao", "Details":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, id):
        """
        deleta uma coleçao
        """
        
        try:
            collection = DiecastCollection.objects.get(pk = id)
        except DiecastCollection.DoesNotExist:
            return Response({"error":"A coleçao nao foi encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        permission_error = check_collection_ownership(collection, request.user)
        if permission_error:
            return permission_error
        
        collection.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
