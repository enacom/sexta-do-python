"""
objetivo do exemplo: mostrar parametrização
Testes de cálculo do imposto de renda a pagar com tesouro selic
Regra: atendimento da tabela regressiva. Aliquota aplicada sobre o lucro

-------------------------------
período (dias) | alíquota (%)
-------------------------------
      180      |  22.5
-------------------------------
    181-360    |  20
-------------------------------
    361-720    |  17.5
-------------------------------
     720+      |  15
-------------------------------


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
"""
from investimentos.calculadora import total_com_juros
from investimentos.investimentos import Selic, Carteira
import pytest
from datetime import datetime, timedelta


# testes tradicionais
def test_selic_valor_total():
    # arrange
    valor_aplicado = 100
    periodo = 30
    rentabilidade = 0.2

    expected = 100.2

    # act
    result = total_com_juros(
        valor_aplicado=valor_aplicado,
        periodo=periodo,
        rentabilidade=rentabilidade
    )

    # assert
    assert result == expected


# Mark.Parametrize

@pytest.mark.parametrize(("periodo,esperado"), [(30, 0.05),
                                                (181, 0.24),
                                                (365, 0.43),
                                                (730, 0.75)])
def test_selic_imposto_a_pagar(periodo, esperado):
    # arrange
    selic = Selic(valor_inicial=100, rentabilidade=0.2)

    # act
    result = selic.imposto_a_pagar(
        periodo=periodo
    )

    # assert
    assert result == esperado


def test_imposto_medio():
    # arrange
    carteira = Carteira(saldo=5000)
    dias = [
        datetime(2020, 12, 1),  # 30 dias
        datetime(2020, 7, 4),  # 181 dias
        datetime(2020, 1, 2),  # 365 dias
        datetime(2019, 1, 2)  # 730 dias
    ]
    for dia in dias:
        selic = Selic(valor_inicial=100, rentabilidade=0.2)
        carteira.novo_investimento(investimento=selic, data=dia)

    esperado = (0.05 + 0.24 + 0.43 + 0.75) / 4

    result = carteira.imposto_medio(data=datetime(2021, 1, 1))

    assert result == esperado


# fixtures
@pytest.fixture
def carteira_cheia():
    carteira = Carteira(saldo=5000)
    dias = [
        datetime(2020, 12, 1),  # 30 dias
        datetime(2020, 7, 4),   # 181 dias
        datetime(2020, 1, 2),   # 365 dias
        datetime(2019, 1, 2)    # 730 dias
    ]
    for dia in dias:
        selic = Selic(valor_inicial=100, rentabilidade=0.2)
        carteira.novo_investimento(investimento=selic, data=dia)
    return carteira


def test_imposto_medio_com_fixture(carteira_cheia):
    esperado = (0.05 + 0.24 + 0.43 + 0.75) / 4

    result = carteira_cheia.imposto_medio(data=datetime(2021, 1, 1))

    assert result == esperado


"""
Fixtures as factories

Eventualmente pode ser interessante que as fixtures sejam parametrizáveis.
Imagine que eu queira, por exemplo, uma carteira com diferentes quantidade de registro de investimento. Uma carteira com 
2 registros, 3 registros, 4 registros...

Podemos fazer isso por meio de factories (fábricas)! Uma fábrica é básicamente uma função que retorna um objeto
conforme os parâmetros que solicitamos. No exemplo anterior, `carteira_cheia` dentro do teste 
`test_imposto_medio_com_fixture` é uma instância de Carteira. Ao refatorar a fixture para ser uma fábrica, 
`carteira_cheia` será uma função que retorna a instância de carteira com as características que queremos.

O exemplo a seguir parametriza a quantidade de investimentos na carteira
 
"""

@pytest.fixture
def fabrica_de_carteiras():
    def carteira_cheia(
            saldo_inicial: float,
            quantidade_de_investimentos: int,
            data_inicial: datetime = datetime(2020, 1, 1),
            intervalo_de_dias_entre_os_registros: int = 180
    ):
        carteira = Carteira(saldo=saldo_inicial)
        dias = [
            data_inicial + timedelta(intervalo_de_dias_entre_os_registros*i)
            for i in range(quantidade_de_investimentos)
        ]
        for dia in dias:
            selic = Selic(valor_inicial=100, rentabilidade=0.2)
            carteira.novo_investimento(investimento=selic, data=dia)
        return carteira  # retorna a instância de Carteira
    return carteira_cheia  # retorna a função (fábrica)


def test_imposto_medio_com_5_investimentos_com_intervalo_de_180_dias(fabrica_de_carteiras):
    """
    datas:
        01/01/2020, 900 dias atrás, R$ 6.18 de lucro, aliquota 15.0%
        29/06/2020, 720 dias atrás, R$ 4.91 de lucro, aliquota 17.5%
        26/12/2020, 540 dias atrás, R$ 3.66 de lucro, aliquota 17.5%
        24/06/2021, 360 dias atrás, R$ 2.42 de lucro, aliquota 20.0%
        21/12/2021, 180 dias atrás, R$ 1.20 de lucro, aliquota 22.5%
        19/06/2022, hoje          , R$ 0.00 de lucro, -
    :param fabrica_de_carteiras:
    :return:
    """
    carteira = fabrica_de_carteiras(
        saldo_inicial=5000,
        quantidade_de_investimentos=6
    )


    esperado = (0.93 + 0.85 + 0.64 + 0.48 + 0.27 + 0) / 6

    result = carteira.imposto_medio(data=datetime(2022, 6, 16))

    assert result == esperado


# raises
def test_novo_investimento_com_carteira_vazia():
    carteira = Carteira()
    investimento = Selic(valor_inicial=100, rentabilidade=0.5)
    with pytest.raises(Exception) as exc:
        carteira.novo_investimento(investimento, data=datetime(2021, 1, 1))
    assert "Não há saldo suficiente" == str(exc.value)

