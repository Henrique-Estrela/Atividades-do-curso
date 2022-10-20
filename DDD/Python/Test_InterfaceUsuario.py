from Destino import Destino
from DestinoRepository import DestinoRepository
from interfaceUser import InterfaceUser


def test_solicitar_input_usuario():
    
    # Arrange
    Destino_Repository = DestinoRepository()
    Interface = InterfaceUser(Destino_Repository)
 
    # Act

    result= Interface.solicitar_input_usuario()


    # Assert
    assert result == 71 
    assert type(result) == int



def test_exibir_destinos():
    
    # Arrange
    Destino_Repository = DestinoRepository()
    Destino_Repository.lista_destino = []
    teste = Destino(71 , "Salvador")
 
    # Act
    Interface = InterfaceUser(Destino_Repository)


    Destino_Repository.adicioanar_destino(teste)
    
 
    # Act

    result= Interface.exibir_destinos(teste.ddd)


    # Assert
    assert result == "Salvador" 



def test_saida_usuario():
    
    # Arrange
    Destino_Repository = DestinoRepository()
    Destino_Repository.lista_destino = []
    teste = Destino(71 , "Salvador")

    teste1 = 71
 
    # Act
    Destino_Repository.adicioanar_destino(teste)


 
    # Act

    result= Destino_Repository.checa_se_destino_existe(teste1)



    # Assert
    assert result == True 
