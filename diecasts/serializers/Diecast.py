from rest_framework import serializers
from diecasts.models import (
    Diecast,
    CarBrand,
    DiecastBrand,
    Carmodel,
    DiecastModel,
)
from diecasts.utils import get_or_create_instance


class DiecastSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Diecast.
    - Permite criar miniaturas informando apenas os nomes das relações.
    - Retorna os nomes relacionados no GET em vez de IDs.
    """

    # Campos de escrita (para criaçao via nome)
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
        
        
    # -------------------------------
    #      MÉTODOS AUXILIARES
    # -------------------------------
        
    def _resolve_relations(self, validate_data):
        """
        Converte nomes enviados em instâncias relacionadas (get_or_create).
        Usado tanto no create() quanto no update().
        """
        
        relations_fields = {
            "brand":("brand_name", DiecastBrand),
            "name":("model_name", DiecastModel),
            "car_brand":("car_brand_name", CarBrand),
            "car_model":("car_model_name", Carmodel)
        }
        
        relations = {}
        
        for field, (input_name, model_class) in relations_fields.items():
            name = validate_data.pop(input_name, None)
            if name:
                relations[field] = get_or_create_instance(model_class, "name", name)
        return relations
    
    
    def _normalize_input(self, data):
        """Converte todos os nomes enviados para maiúsculo"""
        for field in ["brand_name", "model_name", "car_brand_name", "car_model_name"]:
            data[field] = data[field].upper()
        
        return data
    
    
    # -----------------------------
    #     MÉTODOS PRINCIPAIS
    #------------------------------
        
        
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
            "brand": get_or_create_instance(DiecastBrand, "name", brand_name),
            "name": get_or_create_instance(DiecastModel, "name", model_name),
            "car_brand": get_or_create_instance(CarBrand, "name", car_brand_name),
            "car_model": get_or_create_instance(Carmodel, "name", car_model_name),
        }

        # Cria a miniatura com os relacionamentos resolvidos
        return Diecast.objects.create(**relations, **validated_data)
    
    