from decimal import Decimal
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from pescadores.validators import only_numeric_chars
from .municipio import Municipio
from .endereco import Endereco
from .colonia import Colonia
from .programa_social import ProgramaSocial
from .arte_pesca import ArtePesca
from .area_pesca import AreaPesca

SEXOS = [
    ('m', 'Masculino'),
    ('f', 'Feminino'),
    ('n', 'Não binário'),
]

TIPOS_EMBARCACAO = [
    ('barco', 'Barco'),
    ('bote', 'Bote'),
    ('canoa', 'Canoa'),
    ('jangada', 'Jangada'),
    ('lancha', 'Lancha'),
    ('desembarcado', 'Desembarcado(a)'),
]

TAMANHOS_EMBARCACAO = [
    ('pequeno', 'Pequeno'),
    ('medio', 'Médio'),
    ('grande', 'Grande'),
]

ESCOLARIDADE = [
    ('fundamental_incompleto', 'Ensino fundamental incompleto'),
    ('fundamental_completo', 'Ensino fundamental completo'),
    ('medio_incompleto', 'Ensino médio incompleto'),
    ('medio_completo', 'Ensino médio completo'),
    ('superio_incompleto', 'Ensino superior incompleto'),
    ('superior_completo', 'Ensino superior completo'),
]

class Pescador(models.Model):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(2)], blank=False, null=False)
    sexo = models.CharField(max_length=1, choices=SEXOS, blank=True, null=True)
    apelido = models.CharField(max_length=100, validators=[MinLengthValidator(2)], blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    nome_pai = models.CharField(max_length=100, validators=[MinLengthValidator(2)], blank=True, null=True)
    nome_mae = models.CharField(max_length=100, validators=[MinLengthValidator(2)], blank=True, null=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, validators=[only_numeric_chars, MinLengthValidator(11)], blank=True, null=True)
    matricula_colonia = models.CharField(max_length=20, validators=[only_numeric_chars], blank=True, null=True)
    data_inscricao_colonia = models.DateField(blank=True, null=True)
    tipo_embarcacao = models.CharField(max_length=20, choices=TIPOS_EMBARCACAO, blank=True, null=True)
    tamanho_embarcacao = models.CharField(max_length=20, choices=TAMANHOS_EMBARCACAO, blank=True, null=True)
    proprietario_embarcacao = models.BooleanField(blank=True, null=True)
    escolaridade = models.CharField(max_length=30, choices=ESCOLARIDADE, blank=True, null=True)
    renda_mensal_pesca = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal(0))], blank=True, null=True)
    outra_renda = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(default=True, null=True)
    motivo_inatividade = models.TextField(blank=True, null=True)
    falecido = models.BooleanField(default=False, null=True)
    data_cadastramento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)
    naturalidade = models.ForeignKey(Municipio, on_delete=models.PROTECT, blank=True, null=True)
    colonia = models.ForeignKey(Colonia, on_delete=models.PROTECT, blank=True, null=True)
    programas_sociais = models.ManyToManyField(ProgramaSocial)
    areas_pesca = models.ManyToManyField(AreaPesca)
    artes_pesca = models.ManyToManyField(ArtePesca)

    def delete(self, *args, **kwargs):
        if self.endereco:
            self.endereco.delete()
        return super().delete(*args, **kwargs)

    def __repr__(self):
        return self.nome
    
    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'pescadores'
