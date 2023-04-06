from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        12, "Teste1", "Teste2", "Teste3", "Teste4", "Teste5", "Teste6"
    )
    assert produto.id == 12
    assert produto.nome_do_produto == "Teste1"
    assert produto.nome_da_empresa == "Teste2"
    assert produto.data_de_fabricacao == "Teste3"
    assert produto.data_de_validade == "Teste4"
    assert produto.numero_de_serie == "Teste5"
    assert produto.instrucoes_de_armazenamento == "Teste6"
