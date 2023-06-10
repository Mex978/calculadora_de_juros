from tabulate import tabulate

ANO = 12
PERCENTUAL = 1 / 100
CABECALHO = ["Mês", "Juros", "Total Investido", "Total Juros", "Montante"]

VALOR_INICIAL = 500  # Valor incial. Ex: 500
VALOR_MENSAL = 100  # Valor para depósito mensal. Ex: 100
ANOS = 10  # Quantidade de anos. Ex: 10
TAXA_ANUAL = 10  # Valor da taxa anual. Ex: 10 -> 10%


def formatar_moeda(valor):
    return f"R$ {valor:.2f}".replace(".", ",")


def anual_para_mensal(taxa_anual):
    return ((1 + taxa_anual) ** (1 / ANO)) - 1


if __name__ == "__main__":
    valor_inicial, deposito_mensal, meses = VALOR_INICIAL, VALOR_MENSAL, ANOS * ANO
    taxa_anual = TAXA_ANUAL * PERCENTUAL
    taxa_mensal = anual_para_mensal(taxa_anual)
    juros_total, investimento_total, tabela = 0, 0, [CABECALHO]

    for mes in range(meses):
        valor_inicial, juros = (
            valor_inicial + investimento_total,
            valor_inicial * taxa_mensal,
        )
        juros_total += juros
        investimento_total += deposito_mensal
        tabela.append(
            [
                mes,
                formatar_moeda(juros),
                formatar_moeda(investimento_total),
                formatar_moeda(juros_total),
                formatar_moeda(valor_inicial + investimento_total),
            ]
        )

    print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))
