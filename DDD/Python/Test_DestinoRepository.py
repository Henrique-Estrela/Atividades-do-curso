from Destino import Destino
from DestinoRepository import DestinoRepository
from interfaceUser import InterfaceUser


def adicioanar_destino():
    # Arrange
    Destino_Repository = DestinoRepository()
    Destino_Repository.lista_destino = []
    teste = Destino(71 , "Salvador")
 
    # Act


    Destino_Repository.adicioanar_destino(teste)


    destino_existe_teste = Destino_Repository.checa_se_destino_existe(teste.ddd)
    

    # Assert
    assert destino_existe_teste == True
    

def obter_destino_pelo_ddd():
    # Arrange
    Destino_Repository = DestinoRepository()
    Destino_Repository.lista_destino = []
    teste = Destino(71 , "Salvador")
 
    # Act


    Destino_Repository.adicioanar_destino(teste)

    destino_teste = Destino_Repository.obter_destino_pelo_ddd(teste.ddd)

    
    

    # Assert
    assert destino_teste == 'Salvador'



def test_set_menu_item():
    # Arrange
    Destino_Repository = DestinoRepository()
    Destino_Repository.lista_destino = []
    teste = Destino(71 , "Salvador")
 
    # Act


    Destino_Repository.adicioanar_destino(teste)

    destino_existe_teste = Destino_Repository.checa_se_destino_existe(teste.ddd)
    

    # Assert
    assert destino_existe_teste == True
    
