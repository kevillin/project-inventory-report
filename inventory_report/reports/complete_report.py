from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generate(list) -> str:
        empresa_com_mais_produto = {}
        for item in list:
            if item["nome_da_empresa"] in empresa_com_mais_produto:
                empresa_com_mais_produto[item['nome_da_empresa']] += 1
            else:
                empresa_com_mais_produto[item['nome_da_empresa']] = 1

        retorno_completo = "\nProdutos estocados por empresa:\n"
        for key, value in empresa_com_mais_produto.items():
            retorno_completo += f"- {key}: {value}\n"

        return SimpleReport.generate(list) + retorno_completo
