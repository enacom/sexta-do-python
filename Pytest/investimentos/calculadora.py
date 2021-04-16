def total_com_juros(valor_aplicado, periodo, rentabilidade):
    periodo_em_mes = periodo / 30
    total = valor_aplicado * (1 + (rentabilidade / 100)) ** periodo_em_mes
    return total


def lucro(valor_aplicado, valor_com_juros):
    juros_calculado = round(valor_com_juros - valor_aplicado, ndigits=2)
    return juros_calculado


def imposto_a_pagar(valor_aplicado, periodo, rentabilidade):
    valor_final = total_com_juros(
        valor_aplicado=valor_aplicado,
        periodo=periodo,
        rentabilidade=rentabilidade
    )
    juros_calculado = lucro(
        valor_aplicado=valor_aplicado,
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
