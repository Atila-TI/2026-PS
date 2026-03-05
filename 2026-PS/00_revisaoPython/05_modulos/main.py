# =====================================================
# SISTEMA DE CONVERSÃO DE UNIDADES
# =====================================================
# Disciplina : Programação de Sistemas (PS)
# Aula       : 07 — Revisão: Módulos
# Autor      : [Atila da Nascimento Pereira]
# Data       : [DATA DE HOJE]
# Repositório: https://github.com/[SEU-USUARIO]/2026-PS
# =====================================================

from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes,
)

from utils import cabecalho_secao, formatar_resultado, linha_separadora


def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))
    valor = float(input(" Valor em °C: "))
    print(formatar_resultado("°C → °F", valor, "°C",
celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C → K",  valor, "°C", celsius_para_kelvin(valor),
"K"))
