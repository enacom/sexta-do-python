from dataclasses import dataclass, field
from abc import abstractmethod
from typing import List
from datetime import datetime


@dataclass
class Investimento:
    valor_inicial: float
    rentabilidade: float

    def total_com_juros(self, periodo):
        periodo_em_mes = periodo / 30
        total = self.valor_inicial * (1 + (self.rentabilidade / 100)) ** periodo_em_mes
        return total

    def lucro(self, valor_com_juros):
        juros_calculado = round(valor_com_juros - self.valor_inicial, ndigits=2)
        return juros_calculado

    @abstractmethod
    def imposto_a_pagar(self, periodo):
        pass


class Selic(Investimento):
    def imposto_a_pagar(self, periodo):
        valor_final = self.total_com_juros(
            periodo=periodo
        )
        juros_calculado = self.lucro(
            valor_com_juros=valor_final
        )

        if periodo <= 180:
            aliquota = .225
        elif periodo > 180 and periodo <= 360:
            aliquota = .20
        elif periodo > 361 and periodo < 720:
            aliquota = .175
        else:
            aliquota = .15

        imposto = round(juros_calculado * aliquota, ndigits=2)

        return imposto


@dataclass
class RegistroInvestimento:
    data: datetime
    investimento: Investimento


@dataclass
class Carteira:
    saldo: float = 0
    investimentos: List[RegistroInvestimento] = field(default_factory=list)

    def imposto_medio(self, data: datetime):
        if len(self.investimentos) == 0:
            raise Exception("Carteira vazia")
        imposto_total = 0
        for registro in self.investimentos:
            periodo = data - registro.data
            dias = periodo.days
            imposto_total += registro.investimento.imposto_a_pagar(periodo=dias)

        imposto_medio = imposto_total / len(self.investimentos)
        return imposto_medio

    def novo_investimento(self, investimento: Investimento, data: datetime) -> None:
        if self.saldo >= investimento.valor_inicial:
            registro = RegistroInvestimento(investimento=investimento, data=data)
            self.investimentos.append(registro)
            self.saldo -= investimento.valor_inicial
        else:
            raise Exception("Não há saldo suficiente")