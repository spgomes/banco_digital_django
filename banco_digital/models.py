from datetime import timezone
from django.db import models

class Cliente(models.Model):
    PESSOA_FISICA = 'PF'
    PESSOA_JURIDICA = 'PJ'
    TIPO_CHOICES = [
        (PESSOA_FISICA, 'Física'),
        (PESSOA_JURIDICA, 'Jurídica')
    ]

    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES, default=PESSOA_FISICA)
    cpf= models.CharField(verbose_name='CPF', help_text='Somente números', default=0, unique=True, max_length=11)
    cnpj = models.CharField(verbose_name='CNPJ', help_text='Somente números', default=0, unique=True, max_length=14)
    nome_razao_social = models.CharField(verbose_name='Nome completo ou Razão social', max_length= 80, default='')
    endereco = models.CharField(verbose_name='Endereço completo', max_length= 100, default='')
    telefone = models.CharField(verbose_name='Telefone', help_text='Formato: +DI (DDD) 00000-0000', max_length=20, default='')
    data_nascimento = models.DateField(verbose_name='Data de nascimento', null=True, blank=True)

    def __str__(self):
        return self.nome_razao_social

class Conta(models.Model):
    seed = models.AutoField(primary_key=True, editable=False)
    numero_conta = models.IntegerField(unique=True, verbose_name='Número da conta sem dígito verificador', default=0, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldo = models.FloatField(default=0, editable=False)

