from django.contrib import admin
from pescadores.models import *

admin.site.register([
    AlternativaRenda,
    AreaPesca,
    ArtePesca,
    AtividadeAnterior,
    BeneficioColonia,
    CompradorPescado,
    CursoBeneficiamento,
    DestinoPescado,
    DestinoSobras,
    DificuldadeArea,
    DificuldadePagamento,
    EmissorRgp,
    EstadoCivil,
    FornecedorInsumos,
    FonteRendaDuranteDefeso,
    FrequenciaConsumo,
    FrequenciaPesca,
    GostariaFazerNaoFossePescador,
    HabilidadeOutraArea,
    HorarioPesca,
    ItemEstruturaResidencial,
    LocalTratamento,
    MotivacaoPesca,
    MotivoFilhoSeguirProfissao,
    MotivoNaoParticipouOficinas,
    OpiniaoOficinas,
    ProgramaSocial,
    Projeto,
    RelacaoCompanhia,
    RelacaoParentesco,
    TipoInsumo,
    TipoResidencia,
    TipoSeguroDefeso,
    Transporte,
    UnidadeBeneficiamento,
])

admin.site.register([
    Associacao,
    Comunidade,
    Colonia,
    Endereco,
    Municipio,
    Porto,
])

admin.site.register(Pescador)

class RendaDuranteDefesoInline(admin.TabularInline):
    model = RendaDuranteDefeso
    extra = 0

class CompanhiaInline(admin.TabularInline):
    model = Companhia
    extra = 0

class InsumoInline(admin.TabularInline):
    model = InsumoDoPescador
    extra = 0

@admin.register(PescadorEspecialista)
class PescadorEspecialistaAdmin(admin.ModelAdmin):
    inlines = [
        RendaDuranteDefesoInline,
        CompanhiaInline,
        InsumoInline,
    ]
