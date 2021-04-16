# Pytest Example

objetivo do exemplo: mostrar parametrização, fixtures e raises do pytest

Testes de cálculo do imposto de renda a pagar com tesouro selic

Regra: atendimento da tabela regressiva. Aliquota aplicada sobre o lucro

| Periodo (dias) | Aliquota (em % a.m) |
|----------------|---------------------|
| 180            | 22.5                |
| 181-360        | 20                  |
| 361-720        | 17.5                |
| 720+           | 15                  |


Entradas:

    - valor aplicado (em reais)
    - Período (em dias)
    - Rentabilidade (em % a.m.)
    - Calculo nos periodos fracionados (pro_rata_die ou não aplicado)
   
Saídas:

    - valor total
    - imposto a pagar (em reais)
    - lucro bruto (em reais)
    - lucro liquido (em reais)
