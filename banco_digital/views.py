from django.shortcuts import render
from rest_framework import viewsets
from banco_digital.models import Cliente, Conta
from banco_digital.serializers import ClienteSerializer, ContaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

