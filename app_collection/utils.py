from django.db import models

def get_or_create_instance(model: models.Model, field_name: str, value):
    
    """
    Verifica se existe uma instância de um modelo com determinado valor no campo espeficificado.
    Se existir, ele cria
    
    Args:
        model: Model do Django
        field_name: nome do campo a ser verificado
        value: valor a ser procurado ou atribuído
        
    Returns:
        instance: Objeto existente ou recém-criado
    
    """

    lookup = {field_name: value}
    instance, created = model.objects.get_or_create(**lookup)
    return instance