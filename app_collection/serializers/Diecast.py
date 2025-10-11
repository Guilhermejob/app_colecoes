from rest_framework import serializers
from app_collection.models import (
    Diecast,
    Car_Brand,
    Diecast_Brand,
    Car_model,
    Diecast_Model,
)
from app_collection.utils import get_or_create_instance


class DiecastSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Diecast.
    - Permite criar miniaturas informando apenas os nomes das relações.
    - Retorna os nomes relacionados no GET em vez de IDs.
    """

    # Campos de escrita (para criação via nome)
    brand_name = serializers.CharField(write_only=True, help_text="Nome da marca da miniatura (Diecast Brand)")
    model_name = serializers.CharField(write_only=True, help_text="Nome do modelo da miniatura (Diecast Model)")
    car_brand_name = serializers.CharField(write_only=True, help_text="Nome da marca do carro real")
    car_model_name = serializers.CharField(write_only=True, help_text="Nome do modelo do carro real")

    # Campos de leitura (mostrar nomes em vez de IDs)
    brand = serializers.SlugRelatedField(slug_field="name", read_only=True)
    name = serializers.SlugRelatedField(slug_field="name", read_only=True)
    car_brand = serializers.SlugRelatedField(slug_field="name", read_only=True)
    car_model = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Diecast
        fields = "__all__"

    def create(self, validated_data):
        """
        Cria uma instância de Diecast.
        Busca (ou cria) as instâncias relacionadas a partir dos nomes informados.
        """
        # Extrai os nomes das relações
        brand_name = validated_data.pop("brand_name")
        model_name = validated_data.pop("model_name")
        car_brand_name = validated_data.pop("car_brand_name")
        car_model_name = validated_data.pop("car_model_name")

        # Resolve ou cria as relações
        relations = {
            "brand": get_or_create_instance(Diecast_Brand, "name", brand_name),
            "name": get_or_create_instance(Diecast_Model, "name", model_name),
            "car_brand": get_or_create_instance(Car_Brand, "name", car_brand_name),
            "car_model": get_or_create_instance(Car_model, "name", car_model_name),
        }

        # Cria a miniatura com os relacionamentos resolvidos
        return Diecast.objects.create(**relations, **validated_data)
