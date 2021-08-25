from enum import Enum

from science_api.io import IOBaseClass


class ExampleIO(IOBaseClass):

    def __init__(self, input_data, scenario_id='A0'):
        self.input_data = input_data
        self.scenario_id = scenario_id

    def get_output(self) -> dict:
        responses = list()
        for elem in self.input_data["people"]:
            aux_currency = Currency[elem['unit'].upper()]
            responses.append(
                f"hello {elem['name']}, you have {elem['money']} {aux_currency.value}."
            )

        return {"responses": responses}


class Currency(Enum):
    BITCOIN = "BTC"
    BRAZILIAN_REAL = "R$"
