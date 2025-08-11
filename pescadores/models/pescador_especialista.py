from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .alternativa_renda import AlternativaRenda
from .atividade_anterior import AtividadeAnterior
from .beneficio_colonia import BeneficioColonia
from .comprador_pescado import CompradorPescado
from .curso_beneficiamento import CursoBeneficiamento
from .destino_pescado import DestinoPescado
from .destino_sobras import DestinoSobras
from .dificuldade_area import DificuldadeArea
from .dificuldade_pagamento import DificuldadePagamento
from .emissor_rgp import EmissorRgp
from .estado_civil import EstadoCivil
from .fornecedor_insumos import FornecedorInsumos
from .frequencia_consumo import FrequenciaConsumo
from .frequencia_pesca import FrequenciaPesca
from .gostaria_fazer_nao_fosse_pescador import GostariaFazerNaoFossePescador
from .habilidade_outra_area import HabilidadeOutraArea
from .horario_pesca import HorarioPesca
from .item_estrutura_residencial import ItemEstruturaResidencial
from .local_tratamento import LocalTratamento
from .motivacao_pesca import MotivacaoPesca
from .motivo_filho_seguir_profissao import MotivoFilhoSeguirProfissao
from .motivo_nao_participou_oficinas import MotivoNaoParticipouOficinas
from .pescador import Pescador
from .opiniao_oficinas import OpiniaoOficinas
from .recurso_para_compra_insumos import RecursoParaCompraInsumos
from .relacao_parentesco import RelacaoParentesco
from .relacao_tutor import RelacaoTutor
from .tipo_residencia import TipoResidencia
from .tipo_seguro_defeso import TipoSeguroDefeso
from .transporte import Transporte
from .unidade_beneficiamento import UnidadeBeneficiamento

from decimal import Decimal

ESTACOES = [
    ('v', 'Verão'),
    ('i', 'Inverno'),
]

class PescadorEspecialista(models.Model):
    pescador = models.OneToOneField(Pescador, on_delete=models.PROTECT)
    estado_civil = models.ForeignKey(
        EstadoCivil,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    quantidade_filhos = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    reside_no_municipio = models.BooleanField(blank=True, null=True)
    desde_quando_reside_no_municipio = models.DateField(blank=True, null=True)
    tipo_de_residencia = models.ForeignKey(
        TipoResidencia,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    quantidade_moradores_na_casa = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    estrutura_residencial = models.ManyToManyField(
        ItemEstruturaResidencial,
        blank=True,
    )
    quando_deixou_sustentar_familia_apenas_com_pesca = models.DateField(
        blank=True,
        null=True,
    )
    estacao_maior_renda = models.CharField(
        max_length=1,
        choices=ESTACOES,
        blank=True,
    )
    valor_maior_renda = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0))],
        blank=True,
        null=True,
    )
    estacao_menor_renda = models.CharField(
        max_length=1,
        choices=ESTACOES,
        blank=True,
    )
    valor_menor_renda = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    recebe_seguro_defeso = models.BooleanField(blank=True, null=True)
    tipo_seguro_defeso = models.ForeignKey(
        TipoSeguroDefeso,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    quando_comecou = models.DateField(blank=True, null=True)
    com_quem_aprendeu = models.ManyToManyField(
        RelacaoTutor,
        blank=True,
    )
    motivacao = models.ManyToManyField(
        MotivacaoPesca,
        blank=True,
    )
    atividade_anterior = models.ManyToManyField(
        AtividadeAnterior,
        blank=True,
    )
    mora_onde_pesca = models.BooleanField(blank=True, null=True)
    transporte = models.ManyToManyField(
        Transporte,
        blank=True,
    )
    pesca_acompanhado = models.BooleanField(blank=True, null=True)
    # 20. Companhias - reverse relation
    pesca_embarcado = models.BooleanField(blank=True, null=True)
    # Embarcação
    quantidade_parentes_pescadores = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    parentes_pescadores = models.ManyToManyField(
        RelacaoParentesco,
        blank=True,
    )
    frequencia_pesca = models.ForeignKey(
        FrequenciaPesca,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    horario_pesca_mais_frequente = models.ManyToManyField(
        HorarioPesca,
        blank=True,
    )
    duracao_pescaria_dias = models.IntegerField(
        validators=[MinValueValidator(0)],
        blank=True,
        null=True,
    )
    duracao_pescaria_horas = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(24)],
        blank=True,
        null=True,
    )
    data_ultima_pescaria = models.DateField(blank=True, null=True)
    # 28. Insumos - relação reversa
    fornecedores_insumos = models.ManyToManyField(
        FornecedorInsumos,
        blank=True,
    )
    recursos_para_compra_insumos = models.ManyToManyField(
        RecursoParaCompraInsumos,
        blank=True,
    )
    destino_pescado = models.ManyToManyField(
        DestinoPescado,
        blank=True,
    )
    frequencia_consumo_pescado = models.ManyToManyField(
        FrequenciaConsumo,
        blank=True,
    )
    comprador_pescado = models.ManyToManyField(
        CompradorPescado,
        blank=True,
    )
    destino_sobras = models.ManyToManyField(
        DestinoSobras,
        blank=True,
    )
    local_tratamento = models.ManyToManyField(
        LocalTratamento,
        blank=True,
    )
    vinculado_unidade_beneficiamento = models.BooleanField(
        blank=True,
        null=True,
    )
    unidade_beneficiamento = models.ManyToManyField(
        UnidadeBeneficiamento,
        blank=True,
    )
    fez_curso_beneficiamento = models.BooleanField(blank=True, null=True)
    cursos_beneficiamento = models.ManyToManyField(
        CursoBeneficiamento,
        blank=True,
    )
    # 34. RELAÇÃO COM A COLÔNIA
    consegue_pagar_colonia_mensalmente = models.BooleanField(
        blank=True,
        null=True,
    )
    dificuldades_pagamento = models.ManyToManyField(
        DificuldadePagamento,
        blank=True,
    )
    beneficios_colonia = models.ManyToManyField(
        BeneficioColonia,
        blank=True,
    )
    possui_rgp = models.BooleanField(blank=True, null=True)
    emissor_rgp = models.ForeignKey(
        EmissorRgp,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    dificuldades_area = models.ManyToManyField(
        DificuldadeArea,
        blank=True,
    )
    possui_habilidade_outra_area = models.BooleanField(blank=True, null=True)
    habilidades_outras_areas = models.ManyToManyField(
        HabilidadeOutraArea,
        blank=True,
    )
    # 38. Se não pudesse pescar, teria outra alternativa de renda
    possui_alternativas_renda = models.BooleanField(blank=True, null=True)
    alternativas_renda = models.ManyToManyField(
        AlternativaRenda,
        blank=True,
    )
    # 39.
    gostaria_fazer_caso_nao_fosse_pescador = models.ManyToManyField(
        GostariaFazerNaoFossePescador,
        blank=True,
    )
    # 40. Filhos seguissem profissão
    gostaria_filhos_seguissem_profissao = models.BooleanField(
        blank=True,
        null=True,
    )
    motivos_filhos_seguissem_profissao = models.ManyToManyField(
        MotivoFilhoSeguirProfissao,
        blank=True,
    )
    # OUTROS
    grau_dependencia_pesca = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        blank=True,
        null=True,
    )
    ja_participou_oficinas = models.BooleanField(blank=True, null=True)
    opiniao_oficinas = models.ManyToManyField(
        OpiniaoOficinas,
        blank=True,
    )
    motivo_nao_participou_oficinas = models.ManyToManyField(
        MotivoNaoParticipouOficinas,
        blank=True,
    )
    # Observações
    observacoes = models.TextField(blank=True)
    # Entrevistador
    # data_entrevista = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.pescador.nome

    class Meta:
        verbose_name_plural = 'pescadores especialistas'
