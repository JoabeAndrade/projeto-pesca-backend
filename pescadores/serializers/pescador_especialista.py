from rest_framework import serializers
from pescadores.models import PescadorEspecialista

class PescadorEspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PescadorEspecialista
        fields = [
            'id',
            'pescador',
            'estado_civil',
            'quantidade_filhos',
            'reside_no_municipio',
            'desde_quando_reside_no_municipio',
            'tipo_de_residencia',
            'quantidade_moradores_na_casa',
            'estrutura_residencial',
            'quando_deixou_sustentar_familia_apenas_com_pesca',
            'estacao_maior_renda',
            'valor_maior_renda',
            'estacao_menor_renda',
            'valor_menor_renda',
            'recebe_seguro_defeso',
            'tipo_seguro_defeso',
            'quando_comecou',
            'com_quem_aprendeu',
            'motivacao',
            'atividade_anterior',  # 17
            'mora_onde_pesca',
            'transporte',
            'pesca_acompanhado',  # 20
            'pesca_embarcado',
            'frequencia_pesca',
            'horario_pesca_mais_frequente',
            'duracao_pescaria_dias',
            'duracao_pescaria_horas',  # 26
            'data_ultima_pescaria',
            'fornecedores_insumos',
            'recursos_para_compra_insumos',
            'destino_pescado',
            'frequencia_consumo_pescado',
            'comprador_pescado',
            'destino_sobras',  # 30
            'local_tratamento',
            'vinculado_unidade_beneficiamento',
            'unidade_beneficiamento',
            'fez_curso_beneficiamento',
            'cursos_beneficiamento',
            'consegue_pagar_colonia_mensalmente',
            'dificuldades_pagamento',
            'beneficios_colonia',
            'possui_rgp',  # 35
            'emissor_rgp',
            'dificuldades_area',
            'possui_habilidade_outra_area',
            'habilidades_outras_areas',
            'possui_alternativas_renda',
            'alternativas_renda',
            'gostaria_fazer_caso_nao_fosse_pescador',
            'gostaria_filhos_seguissem_profissao',  # 40
            'motivos_filhos_seguissem_profissao',
            'grau_dependencia_pesca',
            'ja_participou_oficinas',
            'opiniao_oficinas',
            'motivo_nao_participou_oficinas',
            'observacoes',
            # 'rendas_durante_defeso',  # reverse relation
        ]
