from django import forms
from django.db import models
from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            'nome_completo','cpf','data_nascimento',
            'numero_casa','placa_veiculo'
        ]
        error_messages = {
            'nome_completo':{
                'required': 'O nome completo do visitante é obrigatorio para o registro'
            },
            'cpf': {
                'required': 'O CPF do visitante  é obrigatorio para o registro'
            },
            'data_nascimento':{
                'required':'A data de nascimento do visitante é obrigatoria para o registro',
                'invalid':'Por favor, informe um formato valido para a data de nascimento (DD/MM/AAAA)'
            },
            'numero_casa':{
                'required':'Por favor, informe o numero da casa a ser visitada'
            }
        }