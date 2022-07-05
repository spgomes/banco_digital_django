from rest_framework import serializers
from banco_digital.models import Cliente, Conta

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Cliente
        fields = ['url', 'id', 'tipo', 'cpf', 'cnpj', 'nome_razao_social', 'endereco', 'telefone', 'data_nascimento']


class ContaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Conta
        fields = ['url', 'numero_conta', 'cliente']
