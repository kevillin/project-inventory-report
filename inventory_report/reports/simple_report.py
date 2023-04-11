from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list) -> str:
        data_fabricacao = SimpleReport.data_fabricacao(list)
        data_validade = SimpleReport.data_validade(list)
        mais_produtos = SimpleReport.mais_produtos(list)
        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            f"Data de validade mais próxima: {data_validade}\n"
            f"Empresa com mais produtos: {mais_produtos}"
        )

    def data_fabricacao(list):
        data_mais_antiga = []
        for item in list:
            data_mais_antiga.append(item["data_de_fabricacao"])
        return min(data_mais_antiga)

    def data_validade(list):
        data_mais_proxima = []
        for item in list:
            if item["data_de_validade"] > datetime.now().strftime("%Y-%m-%d"):
                data_mais_proxima.append(item["data_de_validade"])
        return min(data_mais_proxima)

    def mais_produtos(list):
        empresa_com_mais_produto = {}
        for item in list:
            if item["nome_da_empresa"] in empresa_com_mais_produto:
                empresa_com_mais_produto[item['nome_da_empresa']] += 1
            else:
                empresa_com_mais_produto[item['nome_da_empresa']] = 1
        return max(empresa_com_mais_produto, key=empresa_com_mais_produto.get)
