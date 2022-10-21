from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository


def test_processar_produto():
    # Arrange
    cliente = Cliente(1, "Jefté")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    product1 = Produto(1, "Milk", 50, 10)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(product1)


    

    # Act
    order_product1 = PedidoProduto()
    order_product1.processar_produto(product1, 5)

    # Assert
    assert product1.estoque == 5



def test_baixar_estoque():
    # Arrange
    cliente = Cliente(1, "Jefté")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    quantidade = 9


    product1 = Produto(1, "Milk", 50, quantidade+4)
    product_repository = ProdutoRepository()
    product_repository.adicionar_produto(product1)

    
    # Act
    verify = product1.verificar_estoque(quantidade)
    product1.baixar_estoque(quantidade)


    if verify == True:
        teste = True
    else:
        teste = False
    
    a = product1.estoque

    # Assert
    assert teste == True
    assert a == 4


def test_unit_baixar_estoque():
    # Arrange
    
    quantidade = 9
    product1 = Produto(1, "Milk", 50, quantidade+4)
    
    # Act
    product1.baixar_estoque(quantidade)
    estoque = product1.estoque

    # Assert
    assert estoque == 4

