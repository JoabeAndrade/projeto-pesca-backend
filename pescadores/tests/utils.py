from pescadores.models import Pescador, Porto, Municipio
from datetime import date
from decimal import Decimal

def get_or_create_municipio_dados_validos(nome="Ilhéus", uf="BA"):
    m, _ = Municipio.objects.get_or_create(nome=nome, uf=uf)
    return m

def get_or_create_porto_dados_validos(nome="Porto de Ilhéus", municipio=None):
    if not municipio:
        municipio = get_or_create_municipio_dados_validos()
    p, _ = Porto.objects.get_or_create(nome=nome, municipio=municipio)
    return p

def novo_pescador_dados_validos(
    nome="João da Silva",
    sexo="m",
    apelido="Joãozinho",
    data_nascimento=date(1980, 5, 12),
    nome_pai="Pedro da Silva",
    nome_mae="Maria das Dores",
    rg="123456789",
    cpf="12345678901",
    matricula_colonia="12345",
    data_inscricao_colonia=date(2005, 7, 1),
    tipo_embarcacao="canoa",
    tamanho_embarcacao="pequeno",
    proprietario_embarcacao=True,
    escolaridade="fundamental_completo",
    renda_mensal_pesca=Decimal("1500.00"),
    outra_renda="Trabalho rural",
    ativo=True,
    motivo_inatividade="",
    falecido=False,
    data_cadastramento=date.today(),
    porto_desembarque_principal=None,
):
    if not porto_desembarque_principal:
        porto_desembarque_principal = get_or_create_porto_dados_validos()
    return Pescador(
        nome=nome,
        sexo=sexo,
        apelido=apelido,
        data_nascimento=data_nascimento,
        nome_pai=nome_pai,
        nome_mae=nome_mae,
        rg=rg,
        cpf=cpf,
        matricula_colonia=matricula_colonia,
        data_inscricao_colonia=data_inscricao_colonia,
        tipo_embarcacao=tipo_embarcacao,
        tamanho_embarcacao=tamanho_embarcacao,
        proprietario_embarcacao=proprietario_embarcacao,
        escolaridade=escolaridade,
        renda_mensal_pesca=renda_mensal_pesca,
        outra_renda=outra_renda,
        ativo=ativo,
        motivo_inatividade=motivo_inatividade,
        falecido=falecido,
        data_cadastramento=data_cadastramento,
        porto_desembarque_principal=porto_desembarque_principal,
    )

def create_pescador_dados_validos(
    nome="João da Silva",
    sexo="m",
    apelido="Joãozinho",
    data_nascimento=date(1980, 5, 12),
    nome_pai="Pedro da Silva",
    nome_mae="Maria das Dores",
    rg="123456789",
    cpf="12345678901",
    matricula_colonia="12345",
    data_inscricao_colonia=date(2005, 7, 1),
    tipo_embarcacao="canoa",
    tamanho_embarcacao="pequeno",
    proprietario_embarcacao=True,
    escolaridade="fundamental_completo",
    renda_mensal_pesca=Decimal("1500.00"),
    outra_renda="Trabalho rural",
    ativo=True,
    motivo_inatividade="",
    falecido=False,
    data_cadastramento=date.today(),
    porto_desembarque_principal=None,
):
    if not porto_desembarque_principal:
        porto_desembarque_principal = get_or_create_porto_dados_validos()
    return Pescador.objects.create(
        nome=nome,
        sexo=sexo,
        apelido=apelido,
        data_nascimento=data_nascimento,
        nome_pai=nome_pai,
        nome_mae=nome_mae,
        rg=rg,
        cpf=cpf,
        matricula_colonia=matricula_colonia,
        data_inscricao_colonia=data_inscricao_colonia,
        tipo_embarcacao=tipo_embarcacao,
        tamanho_embarcacao=tamanho_embarcacao,
        proprietario_embarcacao=proprietario_embarcacao,
        escolaridade=escolaridade,
        renda_mensal_pesca=renda_mensal_pesca,
        outra_renda=outra_renda,
        ativo=ativo,
        motivo_inatividade=motivo_inatividade,
        falecido=falecido,
        data_cadastramento=data_cadastramento,
        porto_desembarque_principal=porto_desembarque_principal,
    )
